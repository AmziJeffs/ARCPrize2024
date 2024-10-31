import sys

from dsl import *
from constants import *
from arc_types import *

# Catches syntax warnings in solver defs as errors, so that the solvers don't bother
# trying to execute.
import warnings
warnings.filterwarnings("error")


class Solver():
    """
    Class for holding and manipulating Hodel DSL solvers.
    """

    def __init__(self, solver_text):
        """
        Parse solver text into name, function_text (w/o docstring), docstring,
        and function for calling the solver.
        """
        
        self.name = solver_text.split("(", 1)[0].split(" ")[1]
        self.function_text = self.read_function(solver_text)
        self.docstring = self.read_docstring(solver_text) # Note: self.docstring is stored without indentation
        self.function = self.setup_function()

    def read_function(self, solver_text):
        """
        Read solver_text to get function definition.
        """

        if '    """\n' not in solver_text:
            self.function_text = solver_text
        else:
            defn, _, body = solver_text.split('    """\n')
            self.function_text = defn + body
        return self.function_text

    def read_docstring(self, solver_text):
        """
        Read solver_text to get docstring
        """

        if '    """\n' not in solver_text:
            self.docstring = ""
        else:
            indented_docstring = solver_text.split('    """\n')[1]
            self.docstring = "\n".join(line.strip() for line in indented_docstring.split("\n")).strip()
        return self.docstring

    def setup_function(self):
        """
        Read program_text to self.function.
        """

        exec(self.function_text)
        self.function = eval(self.name)
        return self.function

    def update_docstring(self, new_docstring):
        """
        Set new docstring.

        new_docstring should not include triple quotes. It will be stored
        without indents.
        """

        new_docstring = "\n".join(line.strip() for line in new_docstring.split("\n")).strip()
        self.docstring = new_docstring

    def rename(self, new_name):
        """
        Change name.
        """

        self.function_text = self.function_text.replace(self.name, new_name, 1)
        self.name = new_name
        self.setup_function()

    def num_lines(self):
        """
        Number of lines in function definition of the form xi = call(args).

        Note: self.function_text does not have a trailing linebreak, so we
        can simply count occurrences of linebreaks and subtract one for
        the final return line.
        """

        return self.function_text.count("\n") - 1

    def without_last_k_lines(self, k, include_docstring = True):
        """ 
        Text of function with last k non-return lines removed.
        """

        n_lines = self.num_lines()
        k = min(k, n_lines)

        func_text = self.function_text
        for i in range(k+1):
            func_text = func_text[:func_text.rfind('\n')]

        # Rename return variable if we are just deleting the return line
        if k == 0:
            func_text = func_text.replace("    O = ", f"    x{n_lines} = ")

        if include_docstring:
            if k < n_lines:
                defn, body = func_text.split("\n", 1)
            else:
                defn, body = func_text, ""
            indented_docstring = "    " + self.docstring.replace("\n", "\n    ")
            return defn + "\n" + '    """\n' + indented_docstring + '\n    """\n' + body
        else:
            return func_text

    def __call__(self, input_grid):
        """
        Call self.function on an input.
        """

        return self.function(input_grid)

    def __str__(self):
        """
        Executable string defining the solver, including docstring.
        """

        defn, body = self.function_text.split("\n", 1)
        indented_docstring = "    " + self.docstring.replace("\n", "\n    ") + "\n"
        return defn + "\n" + '    """\n' + indented_docstring + '    """\n' + body

    def __eq__(self, other):
        """
        Two Solvers are equal if their function text matches, but not
        necessarily their names or docstrings.
        """
        if isinstance(other, self.__class__):
            return self.function_text.split('\n', 1)[1] == other.function_text.split('\n', 1)[1]
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """
        Only hashes the lines defining the function, not the docstring or name.
        """
        return hash(self.function_text.split('\n', 1)[1])

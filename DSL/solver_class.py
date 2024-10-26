import sys

from dsl import *
from constants import *
from arc_types import *

sys.path.insert(0, '..')
from misc_utils import *

class Solver():
    """
    TODO
    """

    def __init__(self, solver_text):
        """
        TODO
        """
        
        self.name = solver_text.split("(", 1)[0].split(" ")[1]
        self.function_text = self.read_function(solver_text)
        self.docstring = self.read_docstring(solver_text) # Note: self.docstring is stored without indentation
        self.function = self.setup_function()

    def read_function(self, solver_text):
        """
        Read solver_text to get function definition
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
            self.docstring = "\n".join(line.strip() for line in indented_docstring.split("\n"))
        return self.docstring

    def setup_function(self):
        """
        Read program_text to self.function
        """

        exec(self.function_text)
        self.function = eval(self.name)
        return self.function

    def update_docstring(self, new_docstring):
        """
        new_docstring should not include ''' or similar. It will be inserted between
        triple quotes in program_text. 
        """

        # Make sure input docstring is stripped of indents and leading/trailing newlines
        new_docstring = "\n".join(line.strip() for line in new_docstring.split("\n")).strip()

        # Update self.docstring
        self.docstring = new_docstring

    def randomize_name(self):
        """
        Change name to solve_{random label}
        """

        new_name = f"solve_{random_label()}"
        self.function_text.replace(self.name, new_name)
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

        func_text = self.function_text
        for i in range(k+1):
            func_text = func_text[:func_text.rfind('\n')]

        # Rename return variable if we are just deleting the return line
        if k == 0:
            func_text.replace("    O = ", f"    x{self.num_lines()} = ")

        if include_docstring:
            defn, body = func_text.split("\n", 1)
            indented_docstring = "    " + self.docstring.replace("\n", "\n    ")
            return defn + "\n" + '    """\n' + indented_docstring + '    """\n' + body
        else:
            return func_text

    def __call__(self, input_grid):
        return self.function(input_grid)

    def __str__(self):
        defn, body = self.function_text.split("\n", 1)
        indented_docstring = "    " + self.docstring.replace("\n", "\n    ")
        return defn + "\n" + '    """\n' + indented_docstring + '    """\n' + body

    def __repr__(self):
        return self.__str__()

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

    def __call__(self, input_grid):
        return self.function(input_grid)

    def __str__(self):
        defn, body = self.function_text.split("\n", 1)
        indented_docstring = "    " + self.docstring.replace("\n", "\n    ")
        return defn + "\n" + '    """\n' + indented_docstring + '    """\n' + body

    def __repr__(self):
        return self.__str__()

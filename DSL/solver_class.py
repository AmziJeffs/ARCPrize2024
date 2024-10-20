import sys

from dsl import *
from constants import *
from arc_types import *


class Solver():
    """
    TODO
    """

    def __init__(self, program_text):
        """
        program_text must be in format:
        def program_name(I):
            x1 = ...
            ...
            O = ...
            return O
        """
        self.name = program_text.split("(", 1)[0].split(" ")[1]
        self.program_text = program_text # TODO: Strip \n from end of program text?
        self.function = self.read_function_from_text()
        self.docstring = self.read_docstring_from_text() # Note: self.docstring is stored without indentation

    def read_function_from_text(self):
        """
        Read program_text to self.function
        """
        exec(self.program_text)
        self.function = eval(self.name)
        return self.function

    def read_docstring_from_text(self):
        """
        Read program_text to get docstring
        """
        if '    """\n' not in self.program_text:
            self.docstring = ""
        else:
            indented_docstring = self.program_text.split('    """\n')[1]
            self.docstring = "\n".join(line.strip() for line in indented_docstring.split("\n"))
        return self.docstring

    def update_docstring(self, new_docstring):
        """
        new_docstring should not include ''' or similar. It will be inserted between
        triple quotes in program_text. 
        """
        # Make sure input docstring is stripped of indents and leading/trailing newlines
        new_docstring = "\n".join(line.strip() for line in new_docstring.split("\n")).strip()

        # Update self.docstring
        self.docstring = new_docstring

        # Insert indented docstring in program text
        indented_docstring = "    " + "\n    ".join(line for line in self.docstring.split("\n"))
        if '    """\n' not in self.program_text:
            lines = self.program_text.split("\n")
            lines = [lines[0], '    """', indented_docstring, '    """'] + lines[1:]
            self.program_text = "\n".join(lines)
        else:
            blocks = self.program_text.split('    """\n')
            blocks = [blocks[0], indented_docstring + "\n"] + blocks[2:]
            self.program_text = '    """\n'.join(blocks)

    def __call__(self, input_grid):
        return self.function(input_grid)

    def __str__(self):
        return self.program_text

    def __repr__(self):
        return self.program_text

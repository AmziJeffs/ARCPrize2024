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
        self.name = program_text.split("(I)")[0].split(" ")[1]
        self.program_text = program_text
        self.function = self.update_function_from_text()
        self.docstring = self.update_docstring_from_text()

    def update_function_from_text(self):
        """
        Read program_text to self.function
        """
        exec(self.program_text)
        self.function = eval(self.name)
        return self.function

    def update_docstring_from_text(self):
        """
        Read program_text to get docstring
        """
        if '"""\n' not in self.program_text:
            self.docstring = ""
        else:
            self.docstring = self.program_text.split('"""\n')[1]
        return self.docstring

    def update_docstring(self, new_docstring):
        """
        new_docstring should not include ''' or similar. It will be inserted between
        triple quotes in program_text. 
        """
        self.docstring = new_docstring
        if '"""\n' not in self.program_text:
            lines = self.program_text.split("\n")
            lines = [lines[0], '"""', self.docstring, '"""'] + lines[1:]
            self.program_text = "\n".join(lines)
        else:
            blocks = self.program_text.split('"""\n')
            blocks = [blocks[0], self.docstring + "\n"] + blocks[2:]
            self.program_text = '"""\n'.join(blocks)

    def __call__(self, input_grid):
        return self.function(input_grid)

    def __str__(self):
        return self.program_text

    def __repr__(self):
        return self.program_text

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
        self.update_function_from_text()

    def update_function_from_text(self):
        """
        Read program_text to self.function
        """
        exec(self.program_text)
        self.function = eval(self.name)

    def __call__(self, input_grid):
        return self.function(input_grid)

    def __str__(self):
        return self.program_text

    def __repr__(self):
        return self.program_text

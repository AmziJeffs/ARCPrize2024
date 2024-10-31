import random

def random_label() -> str:
    """
    Random task label consisting of 8 hexidecimal digits lowercase.
    """

    digits = list("0123456789abcdef")
    return "".join([random.choice(digits) for _ in range(8)])


def random_grid(rows = None, cols = None, palette = None):
    """
    A uniformly random grid, with specifiable dimensions and color palette.
    """

    if not rows:
        rows = random.randint(1,30)
    if not cols:
        cols = random.randint(1,30)
    if not palette:
        palette = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    return tuple(tuple(random.choice(palette) for _ in range(cols)) for _ in range(rows))


def grid_to_string(grid):
    """
    Convert grid to string and remove whitespace.
    """

    return str(grid).replace(" ", "")


def grid_to_string_compact(grid):
    """
    Convert grid to string by removing all delimiters except newlines.
    """

    return "\n".join(["".join([str(entry) for entry in row]) for row in grid])


def create_generation_prompt(in_grid, out_grid, name = 'solve'):
    """
    Create a solver with a docstring but no body, for model to complete during
    generation.
    """

    in_str = "\n    ".join(grid_to_string_compact(in_grid).split("\n"))
    out_str = "\n    ".join(grid_to_string_compact(out_grid).split("\n"))

    result = f'''def {name}(I):
    """
    INPUT:
    {in_str}
    OUTPUT:
    {out_str}
    """
    '''

    return result


def create_prompts_from_pairs(in_out_pairs, num_prompts):
    """
    Create generation prompts using a list of in/out grid pairs.
    """

    results = []
    while len(results) < num_prompts:
        results.extend([create_generation_prompt(pair['input'], pair['output']) for pair in in_out_pairs])

    return results[:num_prompts]
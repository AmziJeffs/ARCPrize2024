import random

def random_label() -> str:
    """
    Random task label consisting of 8 hexidecimal digits lowercase.
    """
    digits = list("0123456789abcdef")
    return "".join([random.choice(digits) for _ in range(8)])
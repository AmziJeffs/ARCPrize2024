def solve(I):
    O = upscale(I, TWO)
    return O


def solve(I):
    x1 = numcolors(I)
    x2 = decrement(x1)
    O = upscale(I, x2)
    return O


def solve(I):
    x1 = other(I, ZERO)
    O = upscale(I, TWO)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    O = upscale(I, TWO)
    return O



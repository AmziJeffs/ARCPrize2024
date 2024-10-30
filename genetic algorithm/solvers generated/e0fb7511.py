def solve(I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = sizefilter(x2, ONE)
    x4 = difference(x2, x3)
    x5 = merge(x4)
    O = fill(I, EIGHT, x5)
    return O



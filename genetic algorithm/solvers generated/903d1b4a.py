def solve(I):
    x1 = replace(I, THREE, NEG_ONE)
    x2 = dmirror(x1)
    x3 = papply(pair, x1, x2)
    x4 = lbind(apply, maximum)
    x5 = apply(x4, x3)
    x6 = cmirror(x5)
    x7 = papply(pair, x5, x6)
    x8 = apply(x4, x7)
    x9 = hmirror(x8)
    x10 = papply(pair, x8, x9)
    x11 = apply(x4, x10)
    x12 = vmirror(x11)
    x13 = papply(pair, x12, x11)
    O = apply(x4, x13)
    return O


def solve(I):
    x1 = replace(I, THREE, ZERO)
    x2 = dmirror(x1)
    x3 = papply(pair, x1, x2)
    x4 = lbind(apply, maximum)
    x5 = apply(x4, x3)
    x6 = cmirror(x5)
    x7 = papply(pair, x5, x6)
    x8 = apply(x4, x7)
    O = cmirror(x8)
    return O



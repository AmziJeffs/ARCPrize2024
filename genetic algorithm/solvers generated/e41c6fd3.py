def solve(I):
    x1 = objects(I, T, T, T)
    x2 = ofcolor(I, EIGHT)
    x3 = lowermost(x2)
    x4 = lbind(subtract, x3)
    x5 = chain(toivec, x4, lowermost)
    x6 = fork(shift, identity, x5)
    x7 = merge(x1)
    x8 = cover(I, x7)
    x9 = mapply(x6, x1)
    O = paint(x8, x9)
    return O


def solve(I):
    x1 = objects(I, T, F, T)
    x2 = ofcolor(I, EIGHT)
    x3 = lowermost(x2)
    x4 = lbind(subtract, x3)
    x5 = chain(toivec, x4, lowermost)
    x6 = fork(shift, identity, x5)
    x7 = merge(x1)
    x8 = cover(I, x7)
    x9 = mapply(x6, x1)
    O = paint(x8, x9)
    return O



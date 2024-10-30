def solve(I):
    x1 = leastcolor(I)
    x2 = height(I)
    x3 = vsplit(I, x2)
    x4 = lbind(recolor, TWO)
    x5 = rbind(ofcolor, x1)
    x6 = chain(x4, delta, x5)
    x7 = fork(paint, identity, x6)
    x8 = apply(x7, x3)
    O = merge(x8)
    return O



def solve(I):
    x1 = shape(I)
    x2 = multiply(x1, x1)
    x3 = canvas(ZERO, x2)
    x4 = leastcolor(I)
    x5 = ofcolor(I, x4)
    x6 = lbind(multiply, x1)
    x7 = apply(x6, x5)
    x8 = asobject(I)
    x9 = lbind(shift, x8)
    x10 = mapply(x9, x7)
    O = paint(x3, x10)
    return O


def solve(I):
    x1 = leastcolor(I)
    x2 = ofcolor(I, x1)
    x3 = shape(I)
    x4 = multiply(x3, x3)
    x5 = canvas(ZERO, x4)
    x6 = rbind(multiply, x3)
    x7 = apply(x6, x2)
    x8 = asobject(I)
    x9 = lbind(shift, x8)
    x10 = mapply(x9, x7)
    O = paint(x5, x10)
    return O



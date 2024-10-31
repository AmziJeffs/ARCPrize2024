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



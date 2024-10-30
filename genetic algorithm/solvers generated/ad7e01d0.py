def solve(I):
    x1 = ofcolor(I, FIVE)
    x2 = shape(I)
    x3 = multiply(x2, x2)
    x4 = canvas(ZERO, x3)
    x5 = rbind(multiply, x2)
    x6 = apply(x5, x1)
    x7 = asobject(I)
    x8 = lbind(shift, x7)
    x9 = mapply(x8, x6)
    O = paint(x4, x9)
    return O



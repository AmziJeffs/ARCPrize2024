def solve(I):
    x1 = palette(I)
    x2 = other(x1, ZERO)
    x3 = shape(I)
    x4 = multiply(x3, x3)
    x5 = canvas(ZERO, x4)
    x6 = ofcolor(I, x2)
    x7 = lbind(shift, x6)
    x8 = shape(I)
    x9 = rbind(multiply, x8)
    x10 = apply(x9, x6)
    x11 = mapply(x7, x10)
    O = fill(x5, x2, x11)
    return O


def solve(I):
    x1 = palette(I)
    x2 = other(x1, ZERO)
    x3 = shape(I)
    x4 = multiply(x3,x3)
    x5 = canvas(ZERO, x4)
    x6 = ofcolor(I, x2)
    x7 = lbind(shift, x6)
    x8 = shape(I)
    x9 = rbind(multiply, x8)
    x10 = apply(x9, x6)
    x11 = mapply(x7, x10)
    O = fill(x5, x2, x11)
    return O


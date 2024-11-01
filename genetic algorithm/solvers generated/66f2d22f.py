def solve(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = ofcolor(x1, ZERO)
    x4 = ofcolor(x2, ZERO)
    x5 = intersection(x3, x4)
    x6 = shape(x1)
    x7 = canvas(ZERO, x6)
    O = fill(x7, FIVE, x5)
    return O



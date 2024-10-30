def solve(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = shape(x2)
    x4 = ofcolor(x1, ZERO)
    x5 = ofcolor(x2, ZERO)
    x6 = intersection(x4, x5)
    x7 = canvas(ZERO, x3)
    O = fill(x7, FOUR, x6)
    return O



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


def solve(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = shape(x2)
    x4 = ofcolor(x1, ZERO)
    x5 = ofcolor(x2, ZERO)
    x6 = intersection(x4, x5)
    x7 = canvas(ZERO, x3)
    O = fill(x7, FIVE, x6)
    return O


def solve(I):
    x1 = astuple(vsplit, hsplit)
    x2 = rbind(rbind, TWO)
    x3 = rbind(rapply, I)
    x4 = initset(x2)
    x5 = lbind(rapply, x4)
    x6 = chain(first, x3, x5)
    x7 = lbind(apply, numcolors)
    x8 = compose(x7, x6)
    x9 = matcher(x8, TWO_BY_TWO)
    x10 = extract(x1, x9)
    x11 = x10(I, TWO)
    x12 = first(x11)
    x13 = last(x11)
    x14 = palette(x12)
    x15 = palette(x13)
    x16 = intersection(x14, x15)
    x17 = first(x16)
    x18 = shape(x12)
    x19 = canvas(x17, x18)
    x20 = ofcolor(x12, x17)
    x21 = ofcolor(x13, x17)
    x22 = intersection(x20, x21)
    O = fill(x19, FIVE, x22)
    return O



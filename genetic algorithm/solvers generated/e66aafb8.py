def solve(I):
    x1 = ofcolor(I, ZERO)
    x2 = rbind(colorcount, ZERO)
    x3 = lbind(toobject, x1)
    x4 = compose(x2, x3)
    x5 = vmirror(I)
    x6 = hmirror(I)
    x7 = astuple(x5, x6)
    x8 = argmin(x7, x4)
    O = subgrid(x1, x8)
    return O


def solve(I):
    x1 = palette(I)
    x2 = lbind(rbind, sfilter)
    x3 = lbind(compose, flip)
    x4 = lbind(matcher, first)
    x5 = chain(x2, x3, x4)
    x6 = lbind(paint, I)
    x7 = rbind(compose, asobject)
    x8 = dmirror(I)
    x9 = rbind(rapply, x8)
    x10 = chain(first, x9, initset)
    x11 = chain(x10, x7, x5)
    x12 = compose(x6, x11)
    x13 = compose(x7, x5)
    x14 = compose(cmirror, x12)
    x15 = compose(initset, x13)
    x16 = fork(rapply, x15, x14)
    x17 = compose(first, x16)
    x18 = fork(paint, x12, x17)
    x19 = chain(initset, x7, x5)
    x20 = compose(hmirror, x18)
    x21 = fork(rapply, x19, x20)
    x22 = compose(first, x21)
    x23 = fork(paint, x18, x22)
    x24 = chain(initset, x7, x5)
    x25 = compose(vmirror, x23)
    x26 = fork(rapply, x24, x25)
    x27 = compose(first, x26)
    x28 = fork(paint, x23, x27)
    x29 = fork(equality, identity, hmirror)
    x30 = fork(equality, identity, vmirror)
    x31 = fork(equality, identity, cmirror)
    x32 = fork(equality, identity, dmirror)
    x33 = fork(both, x29, x30)
    x34 = fork(both, x31, x32)
    x35 = fork(both, x33, x34)
    x36 = compose(x35, x28)
    x37 = sfilter(x1, x36)
    x38 = lbind(colorcount, I)
    x39 = argmin(x37, x38)
    x40 = x28(x39)
    x41 = ofcolor(I, x39)
    O = subgrid(x41, x40)
    return O


def solve(I):
    x1 = replace(I, ZERO, NEG_ONE)
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
    x14 = apply(x4, x13)
    x15 = ofcolor(I, ZERO)
    O = subgrid(x15, x14)
    return O


def solve(I):
    x1 = ofcolor(I, ZERO)
    x2 = rbind(colorcount, ZERO)
    x3 = lbind(toobject, x1)
    x4 = compose(x2, x3)
    x5 = vmirror(I)
    x6 = hmirror(I)
    x7 = astuple(x5, x6)
    x8 = argmin(x7, x4)
    O = subgrid( x1, x8)
    return O


def solve(I):
    x1 = hmirror(I)
    x2 = ofcolor(I, ZERO)
    O = subgrid(x2, x1)
    return O


def solve(I):
    x1 = ofcolor(I, ZERO)
    x2 = rbind(colorcount, ZERO)
    x3 = lbind(toobject, x1)
    x4 = compose(x2, x3)
    x5 = hmirror(I)
    x6 = vmirror(I)
    x7 = astuple(x5, x6)
    x8 = argmin(x7, x4)
    O = subgrid(x1, x8)
    return O


def solve(I):
    x1 = hmirror(I)
    x2 = vmirror(I)
    x3 = ofcolor(I, ZERO)
    x4 = subgrid(x3, x1)
    x5 = subgrid(x3, x2)
    x6 = palette(x4)
    x7 = contained(ONE, x6)
    O = branch(x7, x5, x4)
    return O



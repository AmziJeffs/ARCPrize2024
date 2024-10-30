def solve(I):
    x1 = astuple(identity, dmirror)
    x2 = astuple(cmirror, vmirror)
    x3 = combine(x1, x2)
    x4 = compose(first, dmirror)
    x5 = chain(size, dedupe, x4)
    x6 = rbind(rapply, I)
    x7 = compose(first, x6)
    x8 = chain(x5, x7, initset)
    x9 = argmax(x3, x8)
    x10 = x9(I)
    x11 = height(x10)
    x12 = width(x10)
    x13 = ofcolor(x10, ZERO)
    x14 = astuple(x11, ONE)
    x15 = crop(x10, ORIGIN, x14)
    x16 = hupscale(x15, x12)
    x17 = fill(x16, ZERO, x13)
    O = x9(x17)
    return O


def solve(I):
    x1 = height(I)
    x2 = width(I)
    x3 = ofcolor(I, ZERO)
    x4 = astuple(x1, ONE)
    x5 = crop(I, ORIGIN, x4)
    x6 = hupscale(x5, x2)
    O = fill(x6, ZERO, x3)
    return O


def solve(I):
    x1 = astuple(identity,dmirror)
    x2 = astuple(cmirror, vmirror)
    x3 = combine(x1, x2)
    x4 = compose(first, dmirror)
    x5 = chain(size, dedupe, x4)
    x6 = rbind(rapply, I)
    x7 = compose(first, x6)
    x8 = chain(x5, x7, initset)
    x9 = argmax(x3, x8)
    x10 = x9(I)
    x11 = height(x10)
    x12 = width(x10)
    x13 = ofcolor(x10, ZERO)
    x14 = astuple(x11, ONE)
    x15 = crop(x10, ORIGIN, x14)
    x16 = hupscale(x15, x12)
    x17 = fill(x16, ZERO, x13)
    O = x9(x17)
    return O


def solve(I):
    x1 = astuple(dmirror, identity)
    x2 = astuple(cmirror, vmirror)
    x3 = combine(x1, x2)
    x4 = compose(first, dmirror)
    x5 = chain(size, dedupe, x4)
    x6 = rbind(rapply, I)
    x7 = compose(first, x6)
    x8 = chain(x5, x7, initset)
    x9 = argmax(x3, x8)
    x10 = x9(I)
    x11 = height(x10)
    x12 = width(x10)
    x13 = ofcolor(x10, ZERO)
    x14 = astuple(x11, ONE)
    x15 = crop(x10, ORIGIN, x14)
    x16 = hupscale(x15, x12)
    x17 = fill(x16, ZERO, x13)
    O = x9(x17)
    return O



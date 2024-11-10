def solve(I):
    x1 = objects(I, F, F, T)
    x2 = first(x1)
    x3 = subgrid(x2, I)
    x4 = dedupe(x3)
    x5 = rot90(x4)
    x6 = dedupe(x5)
    O = rot270(x6)
    return O


def solve(I):
    x1 = lbind(apply, last)
    x2 = compose(positive, first)
    x3 = lbind(interval, ZERO)
    x4 = rbind(x3, ONE)
    x5 = rbind(sfilter, x2)
    x6 = compose(x4, size)
    x7 = fork(pair, x6, identity)
    x8 = chain(x1, x5, x7)
    x9 = rbind(branch, identity)
    x10 = rbind(x9, x8)
    x11 = chain(size, dedupe, first)
    x12 = lbind(equality, ONE)
    x13 = chain(x10, x12, x11)
    x14 = compose(initset, x13)
    x15 = fork(rapply, x14, identity)
    x16 = compose(first, x15)
    x17 = rbind(branch, identity)
    x18 = rbind(x17, x16)
    x19 = chain(x18, positive, size)
    x20 = compose(initset, x19)
    x21 = fork(rapply, x20, identity)
    x22 = compose(first, x21)
    x23 = multiply(TEN, THREE)
    x24 = power(x22, x23)
    x25 = compose(rot90, x24)
    x26 = power(x25, FOUR)
    x27 = x26(I)
    x28 = lefthalf(x27)
    O = tophalf(x28)
    return O


def solve(I):
    x1 = matcher(identity, ZERO)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind(sfilter, x4)
    x6 = compose(dmirror, x5)
    x7 = power(x6, FOUR)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O


def solve(I):
    x1 = objects(I, F, T, T)
    x2 = first(x1)
    x3 = subgrid(x2, I)
    x4 = lefthalf(x3)
    O = tophalf(x4)
    return O


def solve(I):
    x1 = matcher(identity, F)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind(sfilter, x4)
    x6 = compose(dmirror, x5)
    x7 = power(x6, FOUR)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O



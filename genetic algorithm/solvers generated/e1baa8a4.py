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
    x1 = matcher(identity, ZERO)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind(sfilter, x4)
    x6 = compose(dedupe, x5)
    x7 = power(x6, FOUR)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O


def solve(I):
    x1 = matcher(identity, ZERO)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind(sfilter, x4)
    x6 = compose(dmirror, x5)
    x7 = power(dedupe, TWO)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O


def solve(I):
    x1 = matcher(identity, ZERO)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind( sfilter, x4)
    x6 = compose(dmirror, x5)
    x7 = power(x6, FOUR)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O


def solve(I):
    x1 = matcher(identity, identity)
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


def solve(I):
    x1 = matcher(identity,size)
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
    x1 = matcher(identity, rot90)
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
    x1 = matcher(identity, I)
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
    x1 = matcher(identity,ONE)
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
    x1 = matcher(identity, vmirror)
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
    x1 = matcher(identity, size)
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
    x1 = matcher(identity, lefthalf)
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
    x1 = matcher(identity, THREE)
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
    x1 = matcher(identity, apply)
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
    x1 = matcher(identity, T)
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
    x1 = matcher(identity,EIGHT)
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
    x1 = matcher(identity, compose)
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
    x1 = matcher(identity, vsplit)
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
    x1 = matcher(identity, F)
    x2 = compose(flip, x1)
    x3 = rbind(sfilter, x2)
    x4 = chain(positive, size, x3)
    x5 = rbind(sfilter, x4)
    x6 = compose(cmirror, x5)
    x7 = power(x6, FOUR)
    x8 = x7(I)
    x9 = dedupe(x8)
    x10 = dmirror(x9)
    x11 = dedupe(x10)
    O = dmirror(x11)
    return O



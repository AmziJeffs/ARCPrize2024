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



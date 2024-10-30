def solve(I):
    x1 = frontiers(I)
    x2 = merge(x1)
    x3 = color(x2)
    x4 = shape(I)
    x5 = canvas(x3, x4)
    x6 = hconcat(I, x5)
    x7 = objects(x6, T, F, T)
    x8 = apply(uppermost, x7)
    x9 = order(x8, identity)
    x10 = lbind(sfilter, x7)
    x11 = lbind(matcher, uppermost)
    x12 = compose(x10, x11)
    x13 = lbind(apply, color)
    x14 = rbind(order, leftmost)
    x15 = chain(x13, x14, x12)
    x16 = apply(x15, x9)
    O = vmirror(x16)
    return O


def solve(I):
    x1 = frontiers(I)
    x2 = merge(x1)
    x3 = color(x2)
    x4 = merge(x1)
    x5 = fill(I, NEG_ONE, x4)
    x6 = shape(I)
    x7 = canvas(NEG_ONE, x6)
    x8 = hconcat(x5, x7)
    x9 = objects(x8, F, F, T)
    x10 = rbind(other, x3)
    x11 = compose(x10, palette)
    x12 = fork(astuple, x11, ulcorner)
    x13 = apply(x12, x9)
    x14 = merge(x9)
    x15 = fill(I, x3, x14)
    x16 = paint(x15, x13)
    O = compress(x16)
    return O



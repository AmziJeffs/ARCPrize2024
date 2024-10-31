def solve(I):
    x1 = partition(I)
    x2 = fork(recolor, color, backdrop)
    x3 = apply(x2, x1)
    x4 = mfilter(x3, hline)
    x5 = mfilter(x3, vline)
    x6 = paint(I, x4)
    O = paint(x6, x5)
    return O


def solve(I):
    x1 = partition(I)
    x2 = fork(recolor, color, backdrop)
    x3 = apply(x2, x1)
    x6 = mfilter(x3, hline)
    x7 = mfilter(x3, vline)
    x8 = paint(I, x6)
    O = paint(x8, x7)
    return O


def solve(I):

    x1 = identity(I)
    x2 = partition(I)
    x3 = fork(recolor, color, backdrop)
    x4 = apply(x3, x2)
    x5 = mfilter(x4, hline)
    x6 = mfilter(x4, vline)
    x7 = paint(I, x5)
    O = paint(x7, x6)
    return O


def solve(I):

    x1 = initset(I)
    x2 = partition(I)
    x3 = fork(recolor, color, backdrop)
    x4 = apply(x3, x2)
    x5 = mfilter(x4, hline)
    x6 = mfilter(x4, vline)
    x7 = paint(I, x5)
    O = paint(x7, x6)
    return O


def solve(I):
    x1 = partition(I)
    x2 = fork(recolor, color, backdrop)
    x3 = apply(x2, x1)
    x4 = mfilter(x3, hline)
    x5 = mfilter(x3, vline)
    x6 = paint(I, x4)
    x7 = paint(x6, x5)
    x8 = sizefilter(x7, ONE)
    x9 = merge(x8)
    O = fill(x7, NEG_ONE, x9)
    return O



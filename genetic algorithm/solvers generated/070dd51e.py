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



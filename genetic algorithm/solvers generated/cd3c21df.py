def solve(I):
    x1 = objects(I, T, F, T)
    x2 = totuple(x1)
    x3 = apply(color, x2)
    x4 = lbind(sfilter, x3)
    x5 = lbind(matcher, identity)
    x6 = chain(size, x4, x5)
    x7 = matcher(x6, ONE)
    x8 = sfilter(x3, x7)
    x9 = lbind(colorcount, I)
    x10 = argmax(x8, x9)
    x11 = matcher(color, x10)
    x12 = extract(x1, x11)
    O = subgrid(x12, I)
    return O


def solve(I):
    x1 = partition(I)
    x2 = fork(multiply, height, width)
    x3 = argmin(x1, x2)
    O = subgrid(x3, I)
    return O


def solve(I):
    x1 = vmirror(I)
    x2 = fgpartition(x1)
    x3 = order(x2, size)
    x4 = last(x3)
    x5 = remove(x4, x3)
    x6 = compose(toindices, normalize)
    x7 = rbind(upscale, TWO)
    x8 = chain(toindices, x7, normalize)
    x9 = x6(x4)
    x10 = rbind(intersection, x9)
    x11 = chain(size, x10, x8)
    x12 = argmax(x5, x11)
    x13 = subgrid(x12, x1)
    O = vmirror(x13)
    return O



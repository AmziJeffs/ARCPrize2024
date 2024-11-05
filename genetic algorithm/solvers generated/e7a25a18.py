def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x2 = asobject(x20)
    x3 = shift(x2, UNITY)
    O = paint(x9, x3)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, toindices,box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, T, partition, F)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, partition, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I,  T, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height,width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, objects, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1,x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O


def solve(I):
    x1 = objects(I, T, T, F)
    x2 = fork(equality, toindices, box)
    x3 = sfilter(x1, x2)
    x4 = fork(multiply, height, width)
    x5 = argmax(x3, x4)
    x6 = fgpartition(I)
    x7 = merge(x6)
    x8 = difference(x7, x5)
    x9 = subgrid(x5, I)
    x10 = subgrid(x8, I)
    x11 = height(x9)
    x12 = subtract(x11, TWO)
    x13 = height(x10)
    x14 = divide(x12, x13)
    x15 = width(x9)
    x16 = subtract(x15, TWO)
    x17 = width(x10)
    x18 = divide(x16, x17)
    x19 = hupscale(x10, x18)
    x20 = vupscale(x19, x14)
    x21 = asobject(x20)
    x22 = shift(x21, UNITY)
    O = paint(x9, x22)
    return O



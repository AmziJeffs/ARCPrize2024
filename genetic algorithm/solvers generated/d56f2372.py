def solve(I):
    x1 = objects(I, T, T, T)
    x2 = fork(equality, identity, vmirror)
    x3 = extract(x1, x2)
    O = subgrid(x3, I)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = totuple(x1)
    x3 = rbind(subgrid, I)
    x4 = apply(x3, x2)
    x5 = apply(vmirror, x4)
    x6 = papply(equality, x4, x5)
    x7 = pair(x4, x6)
    x8 = extract(x7, last)
    O = first(x8)
    return O


def solve(I):
    x1 = objects(I, T, T, T)
    x2 = totuple(x1)
    x3 = fork(equality, identity, vmirror)
    x4 = extract(x2, x3)
    O = subgrid(x4, I)
    return O


def solve(I):
    x17 = objects(I, T, T, T)
    x18 = fork(equality, identity, vmirror)
    x19 = extract(x17, x18)
    O = subgrid(x19, I)
    return O


def solve(I):
    x7 = objects(I, T, T, T)
    x8 = fork(equality, identity, vmirror)
    x9 = extract(x7, x8)
    O = subgrid(x9, I)
    return O


def solve(I):
    x1 = objects(I, objects, T, T)
    x2 = fork(equality, identity, vmirror)
    x3 = extract(x1, x2)
    O = subgrid(x3, I)
    return O


def solve(I):
    x27 = objects(I, T, T, T)
    x28 = fork(equality, identity, vmirror)
    x29 = extract(x27, x28)
    O = subgrid(x29, I)
    return O



def solve(I):
    x1 = mostcolor(I)
    x2 = hconcat(I, I)
    x3 = upscale(I, THREE)
    x4 = ofcolor(x3, x1)
    x5 = asindices(x3)
    x6 = difference(x5, x4)
    x7 = hconcat(x2, I)
    x8 = vconcat(x7, x7)
    x9 = vconcat(x8, x7)
    O = fill(x9, ZERO, x6)
    return O


def solve(I):
    x1 = shape(I)
    x2 = multiply(x1, x1)
    x3 = canvas(ZERO, x2)
    x4 = mostcolor(I)
    x5 = ofcolor(I, x4)
    x6 = lbind(multiply, x1)
    x7 = apply(x6, x5)
    x8 = asobject(I)
    x9 = lbind(shift, x8)
    x10 = mapply(x9, x7)
    O = paint(x3, x10)
    return O


def solve(I):
    x1 = shape(I)
    x2 = shape(I)
    x3 = multiply(x2, x1)
    x4 = canvas(ZERO, x3)
    x5 = mostcolor(I)
    x6 = ofcolor(I, x5)
    x7 = lbind(multiply, x1)
    x8 = apply(x7, x6)
    x9 = asobject(I)
    x10 = lbind(shift, x9)
    x11 = mapply(x10, x8)
    O = paint(x4, x11)
    return O


def solve(I):
    x1 = shape(I)
    x2 = multiply( x1, x1)
    x3 = canvas(ZERO, x2)
    x4 = mostcolor(I)
    x5 = ofcolor(I, x4)
    x6 = lbind(multiply, x1)
    x7 = apply(x6, x5)
    x8 = asobject(I)
    x9 = lbind(shift, x8)
    x10 = mapply(x9, x7)
    O = paint(x3, x10)
    return O


def solve(I):
    x1 = shape(I)
    x2 = multiply(x1, x1)
    x3 = canvas(ZERO, x2)
    x5 = mostcolor(I)
    x6 = ofcolor(I, x5)
    x7 = lbind(multiply, x1)
    x8 = apply(x7, x6)
    x9 = asobject(I)
    x10 = lbind(shift, x9)
    x11 = mapply(x10, x8)
    O = paint(x3, x11)
    return O


def solve(I):
    x1 = partition(I)
    x2 = fork( multiply, first, last)
    x3 = shape(I)
    x4 = multiply(x3, x3)
    x5 = canvas(ZERO, x4)
    x6 = mostcolor(I)
    x7 = ofcolor(I, x6)
    x8 = lbind(multiply, x3)
    x9 = apply(x8, x7)
    x10 = asobject(I)
    x11 = lbind(shift, x10)
    x12 = mapply(x11, x9)
    O = paint(x5, x12)
    return O



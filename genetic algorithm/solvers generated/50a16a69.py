def solve(I):
    x1 = asindices(I)
    x2 = box(x1)
    x3 = toobject(x2, I)
    x4 = mostcolor(x3)
    x5 = asobject(I)
    x6 = matcher(first, x4)
    x7 = compose(flip, x6)
    x8 = sfilter(x5, x7)
    x9 = hperiod(x8)
    x10 = vperiod(x8)
    x11 = width(I)
    x12 = width(x8)
    x13 = subtract(x11, x12)
    x14 = add(x13, TWO)
    x15 = height(I)
    x16 = height(x8)
    x17 = subtract(x15, x16)
    x18 = add(x17, TWO)
    x19 = rbind(multiply, x9)
    x20 = invert(x14)
    x21 = interval(x20, x14, ONE)
    x22 = apply(x19, x21)
    x23 = rbind(multiply, x10)
    x24 = invert(x18)
    x25 = interval(x24, x18, ONE)
    x26 = apply(x23, x25)
    x27 = product(x26, x22)
    x28 = lbind(shift, x8)
    x29 = mapply(x28, x27)
    x30 = index(I, ORIGIN)
    x31 = equality(x30, x4)
    x32 = flip(x31)
    x33 = asindices(I)
    x34 = urcorner(x33)
    x35 = index(I, x34)
    x36 = equality(x35, x4)
    x37 = flip(x36)
    x38 = asindices(I)
    x39 = lrcorner(x38)
    x40 = index(I, x39)
    x41 = equality(x40, x4)
    x42 = flip(x41)
    x43 = asindices(I)
    x44 = llcorner(x43)
    x45 = index(I, x44)
    x46 = equality(x45, x4)
    x47 = flip(x46)
    x48 = multiply(x32, LEFT)
    x49 = multiply(x37, UP)
    x50 = add(x48, x49)
    x51 = multiply(x42, RIGHT)
    x52 = multiply(x47, DOWN)
    x53 = add(x51, x52)
    x54 = add(x50, x53)
    x55 = shift(x29, x54)
    O = paint(I, x55)
    return O


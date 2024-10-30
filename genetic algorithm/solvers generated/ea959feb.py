def solve(I):
    x1 = height(I)
    x2 = vsplit(I, x1)
    x3 = apply(asobject, x2)
    x4 = apply(hperiod, x3)
    x5 = minimum(x4)
    x6 = width(I)
    x7 = hsplit(I, x6)
    x8 = apply(asobject, x7)
    x9 = apply(vperiod, x8)
    x10 = minimum(x9)
    x11 = matcher(hperiod, x5)
    x12 = sfilter(x3, x11)
    x13 = mapply(palette, x12)
    x14 = matcher(vperiod, x10)
    x15 = sfilter(x8, x14)
    x16 = mapply(palette, x15)
    x17 = palette(I)
    x18 = combine(x13, x16)
    x19 = rbind(contained, x18)
    x20 = argmin(x17, x19)
    x21 = asobject(I)
    x22 = matcher(first, x20)
    x23 = compose(flip, x22)
    x24 = sfilter(x21, x23)
    x25 = height(I)
    x26 = divide(x25, x10)
    x27 = increment(x26)
    x28 = width(I)
    x29 = divide(x28, x5)
    x30 = increment(x29)
    x31 = invert(x27)
    x32 = interval(x31, x27, ONE)
    x33 = invert(x30)
    x34 = interval(x33, x30, ONE)
    x35 = product(x32, x34)
    x36 = astuple(x10, x5)
    x37 = lbind(multiply, x36)
    x38 = apply(x37, x35)
    x39 = lbind(shift, x24)
    x40 = mapply(x39, x38)
    O = paint(I, x40)
    return O


def solve(I):
    x1 = palette(I)
    x2 = objects(I, T, T, T)
    x3 = lbind(colorfilter, x2)
    x4 = compose(size, x3)
    x5 = valmin(x1, x4)
    x6 = matcher(x4, x5)
    x7 = sfilter(x1, x6)
    x8 = lbind(colorcount, I)
    x9 = argmin(x7, x8)
    x10 = asobject(I)
    x11 = matcher(first, x9)
    x12 = compose(flip, x11)
    x13 = sfilter(x10, x12)
    x14 = lbind(contained, x9)
    x15 = compose(flip, x14)
    x16 = sfilter(I, x15)
    x17 = asobject(x16)
    x18 = hperiod(x17)
    x19 = dmirror(I)
    x20 = sfilter(x19, x15)
    x21 = asobject(x20)
    x22 = hperiod(x21)
    x23 = astuple(x22, x18)
    x24 = lbind(multiply, x23)
    x25 = neighbors(ORIGIN)
    x26 = mapply(neighbors, x25)
    x27 = apply(x24, x26)
    x28 = lbind(shift, x13)
    x29 = mapply(x28, x27)
    O = paint(I, x29)
    return O


def solve(I):
    x1 = height(I)
    x2 = vsplit(I, ONE)
    x3 = apply(asobject, x2)
    x4 = apply(hperiod, x3)
    x5 = minimum(x4)
    x6 = width(I)
    x7 = hsplit(I, x6)
    x8 = apply(asobject, x7)
    x9 = apply(vperiod, x8)
    x10 = minimum(x9)
    x11 = matcher(hperiod, x5)
    x12 = sfilter(x3, x11)
    x13 = mapply(palette, x12)
    x14 = matcher(vperiod, x10)
    x15 = sfilter(x8, x14)
    x16 = mapply(palette, x15)
    x17 = palette(I)
    x18 = combine(x13, x16)
    x19 = rbind(contained, x18)
    x20 = argmin(x17, x19)
    x21 = asobject(I)
    x22 = matcher(first, x20)
    x23 = compose(flip, x22)
    x24 = sfilter(x21, x23)
    x25 = height(I)
    x26 = divide(x25, x10)
    x27 = increment(x26)
    x28 = width(I)
    x29 = divide(x28, x5)
    x30 = increment(x29)
    x31 = invert(x27)
    x32 = interval(x31, x27, ONE)
    x33 = invert(x30)
    x34 = interval(x33, x30, ONE)
    x35 = product(x32, x34)
    x36 = astuple(x10, x5)
    x37 = lbind(multiply, x36)
    x38 = apply(x37, x35)
    x39 = lbind(shift, x24)
    x40 = mapply(x39, x38)
    O = paint(I, x40)
    return O


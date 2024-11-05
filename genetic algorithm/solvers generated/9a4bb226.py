def solve(I):
    x1 = asindices(I)
    x2 = shape(I)
    x3 = objects(I, F,421, T)
    x4 = argmax(x3, numcolors)
    x5 = mostcolor(x4)
    x6 = normalize(x4)
    x7 = mostcolor(I)
    x8 = shape(x4)
    x9 = canvas(x7, x8)
    O = paint(x9, x6)
    return O



def sliceArea(f, x1, x2, max_e):
    y1 = f(x1)
    y2 = f(x2)
    xm = (x1 + x2)/2
    ym = f(xm)
    area_12 = (x1 - x2) * (y2 + y1) / 2.0
    area_1m = (xm - x1) * (y1 + ym) / 2.0
    area_m2 = (x2 - xm) * (y2 + ym) / 2.0
    area_1m2 = area_1m + area_m2
    e = (area_1m2 - area_12) / area_1m2
    if abs(e) < max_e:
        return area_1m2
    return sliceArea(f, x1, xm, max_e) + sliceArea(f, xm, x2, max_e)


def adaptive(f, a, b, n, max_e):
    dx = float(b-a)/n
    result = 0
    x = a
    for i in range(1,n):
        result = result + sliceArea(f, x, x+dx, max_e)
        x = x + dx
        i += 1
    return result


def func(x):
    y = x
    return y


z = adaptive(func, 0, 10, 1000, 100)
print(z)

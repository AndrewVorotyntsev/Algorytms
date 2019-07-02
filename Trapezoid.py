def trapezoid(f, a, b, n):
    dx = float(b-a)/n
    result = 0
    x = a
    for i in range(1,n):
        result = result + dx * (f(x) + f(x + dx))/2
        x = x + dx
        i += 1
    return result


def func(x):
    y = x
    return y


z = trapezoid(func, 0, 10, 1000)
print(z)

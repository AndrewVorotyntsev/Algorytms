def rectangle(f, a, b, n):
    dx = float(b-a)/n
    result = 0
    x = a
    for i in range(1, n):
        result = result + dx * f(x)
        x = x + dx
        i += 1
    return result


def func(x):
    y = x
    return y


z = rectangle(func, 0, 10, 1000)
print(z)
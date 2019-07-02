import random
def monteKarlo(f, a, b ,n):
    # Случайные величины
    v = []
    for i in range(0, n-1):
        v.append(random.uniform(a, b))
    # Значения в случайных точках
    u = []
    for i in range(0, n-1):
        p = f(v[i])
        u.append(p)
    s = 0
    for k in range (1,n):
        s = s + u[i]
    return float((b-a)*s)/n


def func(x):
    y = x
    return y


z = monteKarlo(func, 0, 10, 10000)
print(z)



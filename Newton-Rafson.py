def NewtonRafson(f,dfdx, initial_guess,e):
    x = initial_guess
    for i in range(1, 100):
        y = float(f(x))
        if abs(y) < e:
            break
        x = x - (y / dfdx(x))
        i += 1
    return x

def func(x):
    y = x**2 - 20 * x + 100
    return y


def derivative(x):
    y = 2 * x  - 20
    return y

print(NewtonRafson(func, derivative, 10.1, 0.1))
import random


def MonteCarlo(f, a, b, n):
    s = 0
    for k in range(1, n + 1):
        x = random.uniform(a, b);
        s += f(x);
    I = (float(b - a) / k) * s
    return I


# Подъинтегральная функция
def func(x):
    y = x
    return y


# Вызов функции
I = MonteCarlo(func,0, 10, 100)
print(I)

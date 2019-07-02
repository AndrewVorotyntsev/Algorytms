def decToBin(x):
    # Остаток
    c = x % 2
    # Целая часть
    x = x // 2
    # Целую часть также представляем в двоичном виде
    if x > 0:
        decToBin(x)
    print(c)


b = [1, 0, 1, 0]
def decFromBin(b):
    h = len(b)-1
    a = 0
    for j in range(0, h ,1):
        # Обратить внимание на шаг -1
        for i in range(h, 0, -1):
            a = a + b[j] * 2**i
    return a


d = decFromBin(b)
print(d)
print("длинна" ,len(b)-1)





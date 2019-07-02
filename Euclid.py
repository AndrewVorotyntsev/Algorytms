def euclid(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


d = euclid(21,14)
print(d)
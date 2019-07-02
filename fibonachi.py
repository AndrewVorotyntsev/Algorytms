def fibonachi(x):
    f1 = f2 = fs = 1
    print(f1)
    print(f2)
    m = 0
    t = True
    while t is not False :
        fs = f1 + f2
        f1 = f2
        f2 = fs
        if fs > x :
            t = False
        else:
            print(fs)
            t = True
    return f2


def fibonachi2(n):
    f1 = f2 = fs = 1
    m = 0
    while m < n-2 :
        fs = f1 + f2
        f1 = f2
        f2 = fs
        m += 1
    return fs


def recFibonacci(n):
    if n <=1 :
        return n
    return recFibonacci(n-1) + recFibonacci(n-2)



d = fibonachi2(9)
print(d)
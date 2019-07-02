def fill(n):
    a = []
    for i in range(1, n+1):
        a.append(i)
    return a


def printing(lst):
    for i in range(0, len(lst)):
        print(lst[i])

a = fill(10)
printing(a)


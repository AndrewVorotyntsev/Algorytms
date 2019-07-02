def det(a):
    res = 1
    n = len(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
            res *= -1
        # убеждаемся, что матрица не вырожденная
        if a[i][i] == 0:
            return 0
        res *= a[i][i]
        # "обнуляем" элементы в текущем столбце
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]
    return res

A = [1,0,0,2,2,0,0,0,1]
d = det(A)
print(d)
def sieve(n):
    a = []
    for i in range(n+1):
        a.append(i)
    print(a)
    a[1] = 0
    i = 2
    while i <= n:
        # Если значение ячейки до этого не было обнулено,
        # в этой ячейке содержится простое число.
        if a[i] != 0:
            j = i + i
            while j <= n:
                # это число составное, поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу, которое кратно i (оно на i больше)
                j = j + i
        i += 1
    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)
    # удаляем ноль
    a.remove(0)
    print(a)
    return a


k = int(input())
sieve(k)

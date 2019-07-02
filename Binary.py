def binary(x, lst):
    a = 0
    b = len(lst)-1
    answer = None
    while a <= b:
        m = (a + b)//2
        if lst[m] == x:
            answer = m
            break
        elif lst[m] > x:
            b = m-1
        elif lst[m] < x:
            a = m+1
    return answer


q = [1, 5, 9, 14, 25, 31, 50]
print(binary(14, q))

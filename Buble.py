def sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        i += 1
    return lst

q = [5 , 9 ,13 ,2 , 47 ,65 , 87,12 , 14]
print(sort(q))
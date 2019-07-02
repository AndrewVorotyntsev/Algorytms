def sort(lst):
    n = len(lst)
    for i in range(n):
        #Выбираем ключ , то что будем перемещать
        k = lst[i]
        # Место для перемещения
        j = i
        # Пока ключ меньше предыдущих элементов или пока массив не закончится передвигаем
        while (lst[j-1] > k) and (j > 0):
            lst[j] = lst[j-1]
            j = j - 1
        lst[j] = k
        #print(lst)
    return lst

q = [2,6,4,3,1,5]
print(sort(q))
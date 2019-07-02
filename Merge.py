def merge(left_lst, right_lst):
    # создаем отсортированный массив
    sorted_lst = []
    # начинаем с нуля
    left_index = right_index = 0
    # Длинны правой и левой части
    l, r = len(left_lst), len(right_lst)
    # Пробегаем по всей длинне
    for i in range(l+r):
        # Если отсортированный список меньше исходных
        if left_index < l and right_index < r:
            # Сравниваем первые элементы слева и справа и добавляем меньший в отсортированный список
            if left_lst[left_index] <= right_lst[right_index]:
                sorted_lst.append(left_lst[left_index])
                left_index += 1
            else:
                sorted_lst.append(right_lst[right_index])
                right_index += 1
        # Если отсортированный список больше исходных, то начинаем добавлять в тот что еще не закончился
        elif left_index == l:
            sorted_lst.append(right_lst[right_index])
            right_index += 1
        elif right_index == r:
            sorted_lst.append(left_lst[left_index])
            left_index += 1
    return sorted_lst


def merge_sort(lst):
    # если список состоит из одного элемента возвращаем его
    if len(lst) == 1 :
        return lst
    # Находим середину , округляем до целого
    mid = len(lst)//2
    # В левую часть , то что меньше середины , в правую то что больше середины
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)

q = [5, 9 , 56 , 78 , 54 ,23 ,41 ,57, 75 ,4,12,1]
q = merge_sort(q)
print(q)
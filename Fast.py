import random


def fast_sort(lst):
    # Если список состоит из одного элемента возвращаем его
    if len(lst) <= 1:
        return lst
    else:
        # выбираем рандомное число
        q = random.choice(lst)
        # создаем три списка:для меньших,больших , случайного числа
        less = []
        base = []
        more = []
        # Проходим по всем значениям массива
        for n in lst:
            # Если меньше , то в массив меньших
            if n < q:
                less.append(n)
            # Обратить внимание на elif
            # Если больше , то в массив больших
            elif n > q:
                more.append(n)
            #  Иначе в специальный для случайного числа массив
            else:
                base.append(n)
    # Возвращаем три массива , первый и третий сортируем
    return fast_sort(less) + base + fast_sort(more)


a = [ 8 , 6 , 7 ,2 ,3 ,9 ,1]
print(fast_sort(a))

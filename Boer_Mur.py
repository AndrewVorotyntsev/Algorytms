def predCompil(x):
    d = {}
    lenX =len(x)
    for i in range(len(x)):
        # сколько символов с правого края до этой буквы
        d[ord(x[i])] = lenX - i
    return d

def search_BM_Algoritm(s,x):
    d = predCompil(x)
    # k - проход по s
    # j - проход по x
    # i - место начала прохода по s
    lenX = i = j = k = len(x)
    while j > 0 and i <= len(s):
        # совпали, двигаемся дальше (от конца к началу)
        if s[k-1] == x[j-1]:
            k -= 1
            j -= 1
        # иначе, продвигаемся по строке на d и начинаем с правого конца подстроки снова
        else:
            i += d[ord(s[i])]
            j = lenX
            k = i
    if j <= 0:# нашли
        return k
    return None # не нашли


a = 'My name is Andrew'
b = 'Andrew'

print(search_BM_Algoritm(a,b))
q = ["tiger", "wolf","lion","monkey","deer"]
def linear_search(x,a):
    for index,value in enumerate(a):
        if value == x :
            print(index)
    return index


q = ["tiger", "wolf","lion","monkey","deer"]
linear_search("lion",q)
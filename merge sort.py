def mergesort(a):
    n = len(a)
    if (n == 1):
        return a
    list1 = a[0: (n // 2)]
    list2 = a[(n // 2): n]
    list1 = mergesort(list1)
    list2 = mergesort(list2)
    return merge(list1, list2)


def merge(a, b):
    c = []
    while (len(a) > 0) and (len(b) > 0):
        if (a[0] > b[0]):
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while (len(a) > 0):
        c.append(a[0])
        a.pop(0)
    while (len(b) > 0):
        c.append(b[0])
        b.pop(0)
    return c


mylist = [14, 335765756, 76, 988, 8, 79796686683756868768769859487534658358346756767878, 0, 444]
print(mylist)
print(mergesort(mylist))
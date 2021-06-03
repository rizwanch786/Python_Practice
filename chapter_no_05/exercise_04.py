def even_odd_list(l):
    l1 = []
    l2 = []
    for i in l:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l3 = [l1, l2]
    return l3

l = list(range(0,10))
print (even_odd_list(l))
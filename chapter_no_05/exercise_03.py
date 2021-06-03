def reverse_elements_of_list(l):
    l2 = []
    for i in l:
        l2.append(i[: : -1])
    return l2

l = ['abc','def']
print(reverse_elements_of_list(l)) 
def reverse_elements_of_list(l):
    return [i[: : -1] for i in l]

l = ['abc','def']
print(reverse_elements_of_list(l)) 
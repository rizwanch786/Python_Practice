def filter_common_elements(l1,l2):
    return [i for i in l1 if i in l2]


l1 = [1,2,3,4]
l2 = [5,6,3,4]
print(filter_common_elements(l1,l2))
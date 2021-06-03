# #  method_01

# def reversed_list(l):
#     l.reverse()
#     return l

# # method_02
# def reversed_list(l):
#      return l[: : -1]
 
#  method_03
def reversed_list(l):
    l1 = []
    for i in range (1,len(l)+1):
        l1.append(l.pop())
        i += 1
    return l1

value = ['apple', 'mango', 'banana']
print (reversed_list(value))
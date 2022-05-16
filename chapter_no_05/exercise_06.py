# return no of list inside a list

def sublist_counter(l):
    return sum(type(i) == list for i in l)

l = [1,2,3,[3,2,1],4,5,3,[8,7,6]]
print(sublist_counter(l)) 
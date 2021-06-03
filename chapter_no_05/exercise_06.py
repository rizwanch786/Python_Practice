# return no of list inside a list

def sublist_counter(l):
    count  = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

l = [1,2,3,[3,2,1],4,5,3,[8,7,6]]
print(sublist_counter(l)) 
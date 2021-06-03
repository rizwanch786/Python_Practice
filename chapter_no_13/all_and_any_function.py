# All() : if all numbers in the list are True then it return True otherwise rturn False
numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6]
numbers3 = [1,3,5,7,9]

print (all([n%2 == 0 for n in numbers1]))
print (all([n%2 == 0 for n in numbers2]))
print (all([n%2 == 0 for n in numbers3]))

# Any() : if atleast one number in the list is true then it return true if all numbers in the list are false then it return false
print (any([n%2 == 0 for n in numbers1]))
print (any([n%2 == 0 for n in numbers2]))
print (any([n%2 == 0 for n in numbers3]))

# PRACTICE

def mysum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong input"
print(mysum(1,2,3,4,5,6,7,8,9,10))
print(mysum(1,2,'Rizwan'))
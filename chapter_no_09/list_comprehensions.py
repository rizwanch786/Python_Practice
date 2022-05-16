# List comprehensions : with the help of list comprehensions we can create of list in one line...

#  create a list of squares from 1 to 10
# list old method
squares = [i**2 for i in range(1,11)]
print (squares)
# list comprehensions method
new_squares = [i**2 for i in range(1,11)]
print (new_squares)

# create a list of negative numbers of 1 to 10
# list old method
negative = [-i for i in range(1,11)]
print (negative)
# list comprehensions method
neg = [-i for i in range (1,11)]
print(neg)

names = ["Rizwan", "Ali", "Khalique"]
n_list = [name[0] for name in names]
print (n_list)
# list comprehensions method
name_list = [n[0] for n in names]
print(name_list)

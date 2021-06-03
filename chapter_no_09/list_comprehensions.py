# List comprehensions : with the help of list comprehensions we can create of list in one line...

#  create a list of squares from 1 to 10
# list old method
squares = []
for i in range(1,11):
    squares.append(i**2)
print (squares)
# list comprehensions method
new_squares = [i**2 for i in range(1,11)]
print (new_squares)

# create a list of negative numbers of 1 to 10
# list old method
negative = []
for i in range(1,11):
    negative.append(-i)
print (negative)
# list comprehensions method
neg = [-i for i in range (1,11)]
print(neg)

# create a list of names display only first letter of every name
# list old method
n_list = []
names = ["Rizwan", "Ali", "Khalique"]
for name in names:
    n_list.append(name[0])
print (n_list)
# list comprehensions method
name_list = [n[0] for n in names]
print(name_list)

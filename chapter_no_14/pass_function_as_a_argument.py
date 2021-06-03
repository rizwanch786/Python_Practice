# we pass function as arguments as passing function in map function
# map
l = [1,2,3,4,5]
def square(a):
    return a**2
print (list(map(square,l)))
# or using lambda expression
print(list(map(lambda a : a**2, l)))
# we define own function that receive an function as parameter
def my_map(func,l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list
# function call
print(my_map(square,l))
# using lambda expression
print(my_map(lambda a : a**2, l))

# list comprehension
def my_map2(func,l):
    return (func(i) for i in l)
print(list(my_map2(square,l)))
print(list(my_map2(lambda a : a**2, l)))
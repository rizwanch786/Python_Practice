# MAP FUNCTION : map function commonly used bcz it reduce the code
# map(function_name, iterable/vriable/list/tupple/etc)
numbers = [1,2,3,4,5,6,7,8,9,10]
# normal function
def sequare(a):
    return a**2
# the above function not iterate it just return onlt one value so, if we want sequare of above list the we pass every elements one by one
# like : [sequare(1),sequare(2),.............,sequare(10)]
# map function
print (map(sequare,numbers)) # It return an object address, if we want to display the values then we convert it into list or itrate, it is iterator only one time only.
print(list(map(sequare,numbers)))
# or 
new_list = []
seq = map(sequare,numbers)
for num in seq:
    print(num)
# using lambda expression inside the map function that can reduce the code
sequares = map(lambda a : a**2, numbers)
print(list(sequares))

# list coprehension
sequares_new = [num**2 for num in numbers]
print(sequares_new)

# Simple way to display list sequares
new_numbers = []
for i in numbers:
    new_numbers.append(i**2)
print(new_numbers)

# Example using map function that take a list and return length of every string in the list
string = ['abc', 'abcd', 'abcde']
leng = map(len,string)
# 1)
# for i in leng:
#     print(i)
# 2)
# print (list(leng))
# it iterate only one time, if we use it again and again means use many time then convert it into list and iterate many time
# like:
it = list(leng)
print([i for i in it])
print([i for i in it])
# :-)

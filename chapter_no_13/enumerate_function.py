# ENUMERATE FUNCTION : we ues with for loop to track position of our item in iterable.

# # How we can do this without enumerate function
l = ['Rizwan', 'Ali', 'Khalique']
# pos = 0
# for name in l:
#     print (f"{pos}----->{name}")
#     pos += 1

# # With the help of enumerate function
# for pos, name in enumerate(l):
#      print (f"{pos}----->{name}")   

# Exercise
# Define a fuction that take two arguments
# 1) list containing string
# 2) string that want to find in your list and this function will return index of string in your list and if string is not present then return -1.
def func(l,s):
    for pos, name in enumerate(l):
        if s == name:
            return pos
    return -1

string = 'Ali'
print(func(l,string))
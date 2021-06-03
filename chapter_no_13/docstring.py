# What is docstring?
# docstring is a messange for those user's who use functions

# How to write docstring
# we use triple single quotes '''docstring''' or triple double quotes """docstring""" for writing docstring
# Example
def add (a,b):
    '''this function takes 2 number's and return their sum'''
    return a+b

print(2,4)

# How to see docstring
print (add.__doc__)
# len, max, min, sum, sorted etc
print(len.__doc__)
print(sum.__doc__)

# What is help function?
# if we want to know about any function that function what to do etc then we use help function like:
print(help(sum))
print(help(max))
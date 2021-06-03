def square(a):
    return a**2

# if we assign function name to a variable then the variable work like a function
a = square
print(a(5))
print(a.__name__)
print(square.__name__)
print(a)
print(square)
# the above two statements give same memory address
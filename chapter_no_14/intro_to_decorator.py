# # DECORATOR : inhence/increase the functionality of other function's
# # @ use for decorator

# def fun1():
#     print("This is function 1")

# def fun2():
#     print("This is function 2")

# # if we want to print this ststement 'this function is awesome ' before of every function call then we use decorator function
# def decorator_function(any_function):
#     def wrapper_function():
#         print("This function is awesome")
#         any_function()
#     return wrapper_function

# # now we pass a function that want to display the awesome line first
# # like:
# var = decorator_function(fun1)
# var()

# var1 = decorator_function(fun2)
# var1()

# # or we use senthatic suger (@) sigh before any function defination to use short cut method like:
# @decorator_function
# def func1():
#     print("This is function 1")
# # call
# func1()

# @decorator_function
# def func2():
#     print("This is function 2")
# # call
# func2()

# # decoration part-2
# # if we  want to pass an argument to function then, it give an ERROR.....!
# def decorator_function(any_function):
#     def wrapper_function():
#         print("this a awesome function")
#         any_function()
#     return wrapper_function
# @decorator_function
# def func3(a):
#     print(f"this is a function with argument {a}")
# func3(5)
# # for solving above problem we use *args, **kwargs parameters in inner_function like:
# def decorator_function(any_function):
#     def wrapper_function (*args, **kwargs):
#         print("This is awesome function")
#         any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def func4(a):
#     print(f"this is function with argument {a}")
# # call
# func4(5)

# # returning values from function
# def decorator_function(any_function):
#     def wrapper_function (*args, **kwargs):
#         print("This is awesome function")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def add(a,b):
#     return a + b
# # call
# print(add(5,7))
# # part-3
# if we use docstring like:
# def decorator_function(any_function):
#     def wrapper_function (*args, **kwargs):
#         '''this is wrapper function'''
#         print("This is awesome function")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def add (a,b):
#     '''this is add function'''
#     return a+b
# # if we print docstring of add function then it return wrapper function string like:
# print(add.__doc__)
# print(add.__name__)
# # for solving above problem we import wraps and use @wraps(ant_function ) inside the decorator_function like:
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function (*args, **kwargs):
        '''this is wrapper function'''
        print("This is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add (a,b):
    '''this is add function'''
    return a+b
# now it display the docstring of add_function
print(add.__doc__)
print(add.__name__)
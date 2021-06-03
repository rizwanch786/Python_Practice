# LAMBDA EXPRESSION (anonymous function)
# it use in bulid-in-functions like: map, reduce, filter etc
# Simple function
def add(a,b):
    return a+b
print (add(5,7))
# Lambda expression
add2 = lambda a,b : a+b
print (add2(2,3))

# lambda with if, else
# Simple function
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False
print(is_even(4))
# Short form
def is_even1(a):
    return a%2 == 0   #it return True/False
print(is_even1(5))
# lambda expression
is_even2 = lambda a : True if a%2 == 0 else False
print(is_even2(6))
# Short Form
is_even3 = lambda a : a%2 == 0
print(is_even3(7))
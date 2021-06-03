# normal function
def total(a,b):
    return a+b
print (total(5,7))
# print(total(2,3,4,5,6,7,8,9))
# if we want to pass multiple values in total function then it give an error
# *args: is use too pass miultiple values to a function it make a tupple of passed values

def all_total(*args):
    total = 0
    for i in args:
        total += i
    return total
print (all_total(1,2,3,4,5,6,7,8,9,10))

# *args with normal parameters
def multiply_numbers(a, *args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_numbers(2,2,3))
# the first value pass as nomal argument and the other values become a tupple and received by *args parameter
# pass *args as argument

num = [2,3,4] # it may be a tupple
# print(all_total(num)) #it pass num as a single value its mean it not pass unpack values to the function
print (all_total(*num)) # it unpack the list/tupple 
# FILTER FUNCTION : it is use to filter values from a list/tupple accourding to our need/function that is defined
# below is function that return even value:
def is_even(a):
    return a%2 == 0
# This function take only one value if the value is even then it return True otherwise False
# Now, we want to filter even numbers  fron a list then we use filter function by pass it above function and iterable
numbers = [3,2,1,4,5,6,8,9,10]
even = map (is_even,numbers)
# # 'even' is a referance object. we use for loop or convert it into list/tuple for displaying the values.
# print (list(even))
# or
for num in even:
    print (num)

# use lamba expression inside the filter function that reduce the code like:
e = map (lambda a: a%2 == 0, numbers)
print(tuple(e))

# list coprehension
l_even = [i for i in numbers if i%2 == 0]
print(l_even)

# Simple function
simple_even = []
for i in numbers:
    simple_even.append(i%2 == 0)
print(simple_even)
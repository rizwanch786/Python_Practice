# GENERATOR : are iterators, save time and increase performace. generators are used when we want the sequance only one time only.
# simple function
def nums (n):
    for i in range (1,n+1):
        print(i)
# call
nums(10)
# it generate any time when we want but it take large memory and consume time

# generator function
def numbers(n):
    for i in range (1, n+1):
        yield i
# print(numbers(10)) # it give an geretor object that iterator
# for i in numbers(10):
#     print(i)
# generator generate value only one time not repeated again and again like list etc
# when one value generate it remove the previous value from the memorey, therefore it used when the user not want the sequence again and again it want the sequence only one time.
# prove
g = numbers(10)
for i in g:
    print(i)
for i in g:
    print(i)
# the above loops generate the sequence only one time therefore, it save memory and increase the performace 

# define generator function
# take one argument
# generate a sequence of even numbers from 1 to that number

def is_even(n):
    for i in range (1, n+1):
        if i%2 == 0:
            yield i

print(is_even(10))
even = is_even(10)
for i in even:
    print(i)
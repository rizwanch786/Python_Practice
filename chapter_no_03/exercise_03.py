# sum of n natural numbers
# ask a user for natural number 'n'
# print total from 1-n

n = int (input ("Enter a number: "))
sum = sum(range(1, n + 1))
print (f"Sum: {sum}")
# sum of n natural numbers
# ask a user for natural number 'n'
# print total from 1-n

n = int (input ("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print (f"Sum: {sum}")
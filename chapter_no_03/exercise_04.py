user_input = input ("Enter contianing more than one digit number: ")

sum = 0
i = 0
while i<len(user_input):
    sum += int(user_input[i])
    i += 1
print (f"Sum: {sum}")
user_input = input ("Enter contianing more than one digit number: ")

sum = sum(int(user_input[i]) for i in range(len(user_input)))
print (f"Sum: {sum}")
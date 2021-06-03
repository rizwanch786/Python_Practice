winning_number = 7
user_number = int(input("Enter your number (1-100) : "))
if user_number == winning_number:
    print("you win...!!!!!")
else:
    if user_number<winning_number:
        print("too low")
    else:
        print("too high")
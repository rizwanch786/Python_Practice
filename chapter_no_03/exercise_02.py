user_name = input ("Enter your name: ")
user_age = int (input ("Enter your age: "))

if user_name[0] in ["a", "A"] and user_age >= 10:
    print ("You can watch movie")
else:
    print ("Sorry, you cannot watch movie")
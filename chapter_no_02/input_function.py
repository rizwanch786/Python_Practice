name = input("Enter your name: ")
print ("Hello " + name)

# input function also input a string and we can't concatenate a string with a number therefore, it take input as a string

age = input("Enter your age: ")
print (name + " is " + age + " year old")

# two or more input in single line
name , age = input("Enter your name and age: ").split()
name2 , age2 = input("Enter your name2 and age2: ").split(",")
# """ def is_palindrome (string):
#     for i in range (len(string)):
#         if string[i] == string[-i-1]:
#             return True
#         else:
#             return False """

def is_palindrome (string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    else:
        return False



user_input = input ("Enter a string: ")
b = is_palindrome (user_input)

if b:
    print("Palindrome")
else:
    print ("Not Palindrome")
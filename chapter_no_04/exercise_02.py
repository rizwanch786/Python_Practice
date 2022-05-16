# """ def is_palindrome (string):
#     for i in range (len(string)):
#         if string[i] == string[-i-1]:
#             return True
#         else:
#             return False """

def is_palindrome(string):
    reverse_string = string[::-1]
    return string == reverse_string



user_input = input ("Enter a string: ")
if b := is_palindrome(user_input):
    print("Palindrome")
else:
    print ("Not Palindrome")
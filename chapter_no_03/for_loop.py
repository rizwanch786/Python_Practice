# # start i from 0
# for i in range(10):
#     print(f"Hello world : {i}")
# # strat i from 1
# for i in range(1,11):
#     print (f"Pakistan : {i}")

# *************************************************************************************
# # for loop example_01
# sum = 0
# for i in range (1,11):
#     sum += i
#     i += 1
# print (f"Sum: {sum}")

# # for i in range (1,n+1)
# n = int (input ("Enter a value: "))
# total = 0
# for i in range (1,n+1):
#     total += i
#     i += 1
# print (f"Total: {total}")

# # *************************************************************************************
# # Example_02
# user_input = input ("Enter contiaing more than one digit: ")
# sum = 0
# for i in range (len(user_input)):
#     sum += int(user_input[i])
#     i += 1
# print (f"Total: {sum}")

# # *************************************************************************************
# # Example_03
# user_name = input ("Enter your name: ")
# temp = ""
# for i in range (len(user_name)):
#     if user_name[i] not in temp:
#         temp += user_name[i]
#         print(f"{user_name[i]} : {user_name.count(user_name[i])}")
#     i += 1
import random
winning_number = random.randint(1,100)
# # user_input = int (input("Enter your guess number 1-100 : "))
# count = 1
# # game_over = False

# while True:# not game_over:
#     user_input = int (input("Enter your guess number 1-100 : "))

#     if user_input == winning_number:
#         print (f"You win and you guess in {count} times")
#         break                        # game_over = True
#     else:
#         if user_input > winning_number:
#             print ("Too high")
#             # count += 1
#             # user_input = int (input ("Enter Again: "))
#         else:
#             print ("Too Low")
#             # count += 1
#             # user_input = int (input ("Enter Again: "))
# # Dry coading: don't repeat your-self
#         count += 1
#         continue
#         # user_input = int (input ("Enter Again: "))
print(f"Winner : {winning_number}")
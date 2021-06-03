user_name = input ("Enter your name: ")
i = 0
repeated = ""
while i<len(user_name):
    if user_name[i] not in repeated:
        repeated += user_name[i]
        print (f"{user_name[i]} : {user_name.count(user_name[i])}")
    i += 1
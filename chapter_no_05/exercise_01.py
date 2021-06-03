def sequare_list(l):
    sequare = []
    for i in l:
        sequare.append(i**2)
    return sequare


user_list = list(range(1,5))

print (sequare_list(user_list))
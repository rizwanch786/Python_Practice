def to_power_three(num, *args):
    # if args:
    #     print ("hi you didn't pass args")
    # else:
    #     print (list(args))
    # l = []
    # for i in args:
    #     l.append(i**num)
    # return l
    # list comprehension
    if args:
        return [i**num for i in args]
    else:
        print("hi you didn't pass args")


nums = [1,2,3]
num = 3
print (to_power_three(num, *nums))



# def greater_number(x,y):
#     if x==y:
#         print("Both are equal's")
#     elif x>y:
#         print (f"{x} is greater than {y}")
#     else:
#         print (f"{y} is greater than {x}")

# a = int (input("Enter first value: "))
# b = int (input ("Enter Second value: "))
# greater_number(a,b)
# ************************** OR ****************************************
def fun(x,y):
    if x>y:
        return x
    else:
        return y


a = int (input("Enter first value: "))
b = int (input ("Enter Second value: "))
print (f"Greater value is: {fun(a,b)}")
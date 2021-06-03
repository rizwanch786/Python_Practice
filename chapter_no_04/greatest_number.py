def greatest (x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z


a = int (input ("Enter first value: "))
b = int (input ("Enter second value: "))
c = int (input ("Enter third value: "))
print (f"Greatest value is: {greatest(a,b,c)}")
# Fibonacci_series
# n = 10: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#  mean sum of last 2 digits
# if n = 1 then output: 0
# if n = 2 then output: 0 , 1

def fibonacci_series(n):
    a = 0
    b = 1
    if n == 1:
        print (a)
    elif n == 2:
        print (a,b, end = " ")
    else:
        print (a , b , end = " ")
        for i in range (n-2):
            c = a + b # c = 1, 2, 3, 5, 8,.............., 34 
            a = b # b = 1, 1, 2, 3, 5, ................., 21
            b = c # c = 1, 2, 3, 5, 8, ................., 34
            print (c , end = " ")
            i += 1
# function call
fibonacci_series(10)
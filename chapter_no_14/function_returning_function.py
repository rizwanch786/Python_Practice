def outer_func():
    def inner_func():
        print("inside inner  function")
    return inner_func

var = outer_func() #it return inner function
var() #it call/execute the inner function

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2
var2 = outer_func2("Hi there..!")
var2()

# function returning function is known as closure/ first class function
def is_power(x):
    def calc_power(n):
        return n**x
    return calc_power
# call
cube = is_power(3)
print(cube(2))

square = is_power(2)
print(square(5))
# **kwargs
# kwargs (keyword arguments)
# **kwargs (double star operator)
# it combine all arguments as a dictionary
# kwargs as parameter

def func1(**kwargs):
    print (kwargs)
    print(type(kwargs))

def func2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# call
func1(first_name = "Muhammad", last_name = "Rizwan")
func2(first_name = "Muhammad", last_name = "Rizwan")

# pass as arguments
d = {'Name' : 'Rizwan', 'Roll_No': 40}
func2(**d)
from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("invalid input")
        return wrapper
    return decorator

# we pass any data type what we want
# here we pass a string data type bcz we want to use string concatination function
@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

# call
print(string_join('Rizwan'," ",' Anwar'))
print(string_join('Rizwan', 40))
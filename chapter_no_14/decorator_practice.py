from functools import wraps
def print_function_data(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''this is wrapper function'''
        print(f"you are calling {any_function.__name__} function")
        print(any_function.__doc__)
        return any_function(*args, **kwargs)
    return wrapper_function


@print_function_data
def add(a,b):
    '''This function takes two numbers as argument and return their sum'''
    return a+b

print(add(5,4))

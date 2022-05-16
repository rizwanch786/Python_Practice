# only_int_allow
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wapper(*args, **kwargs):
        if all(type(arg) == int for arg in args):
            return function(*args, **kwargs)
        print("invalid arguments")
    return wapper

@only_int_allow
def add_all(*args):
    return sum(args)

# call
print(add_all(1,2,3,4,5))
print(add_all(1,2,3,'Rizwan'))
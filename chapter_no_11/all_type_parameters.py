# PADK
# simple parametes
# *args
# defult parameters
# **kwargs

def func(name, *args, first_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(first_name)
    print(kwargs)

func('Rizwan', 1,2,3, a=1,b=2)
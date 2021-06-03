l = ['abc', 'tuv', 'xyz']
def reverse_list(l):
    return [values[: : -1] for values in l]

print (reverse_list(l))
# it is not commonaly use

s = set(range(1,11))
print (s)

# Square the above set
s1 = {i**2 for i in s}
print (s1)
# simpe method
s2 = [i**2 for i in s]
print (set(s2))


names = {'Rizwan', 'Ali', 'Khalique'}
# simple
n1 = [name[0] for name in names]
print (set(n1))

# comprehension
n2 = {name[0] for name in names}
print(n2)
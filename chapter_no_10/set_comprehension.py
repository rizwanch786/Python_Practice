# it is not commonaly use

s = set(range(1,11))
print (s)

# Square the above set
s1 = {i**2 for i in s}
print (s1)
# simpe method
s2 = []
for i in s:
    s2.append(i**2)
print (set(s2))


names = {'Rizwan', 'Ali', 'Khalique'}
# simple
n1 = []
for name in names:
    n1.append(name[0])
print (set(n1))

# comprehension
n2 = {name[0] for name in names}
print(n2)
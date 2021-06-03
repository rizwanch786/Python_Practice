# Set: is unordered collection of unique items.
# string, float and interger values only stored in the list and list, tuple and dictionary is not stored in the list.
s = {1,2,3}
print(s)

# Sets are use to remove duplication.
l = [1,2,3,4,5,5,5,5,6,7,7,8]
s1 = set(l)
print(s1)
l1 = list(s1)
print (l1)

# Methods in set
#  Add (): is used to add values  in set
s.add(4)
s.add(5)
print(s)

# remove() : is used too remove value from the set
s.remove(5)
print(s)

# discard() : is used too remove value from the set
s.discard(4)
print(s)

# clear() : used to clear the list
s.clear()
print(s)

# in keyword
in_set = {'a', 'b', 'c'}
if 'a' in in_set:
    print("Present")
else:
    print ("Not Present")

# looping in set
for i in in_set:
    print(i)

# Set maths
# union: "all values from both sets" symbols (|)
# intersection: "Common values only from both sets" symbol (&)
set1 = {1,2,3,4}
set2 = {2,4,5,6,7}
union_set = set1 | set2
intersection_set = set1 & set2
print(union_set)
print(intersection_set)
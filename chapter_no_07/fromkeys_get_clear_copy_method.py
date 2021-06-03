# fromkeys() method: is used to create a dictionary by providing same values of every key

d = dict.fromkeys(['name', 'age'], 'unknown')
d1 = dict.fromkeys(['name', 'age'],['unknown','unkown'])
print(d)
print(d1)

#  get() method: is used to get a  key
user_info = {'name': 'Rizwan', 'age': 21}
print(user_info.get('name'))

if user_info.get('name'):
    print("present")
else:
    print("Not Present")

print(user_info.get('abc'))
# if we want to replace None by any other text then
print(user_info.get('abc','Not Found..!'))

# clear() method: is used to clear a dictionary
d.clear()
print(d)

# copy() method: it make a duplicate copy of a dictionary, if we change anything then it not effect the original dictionary, it work like pass by value
dic = user_info.copy()
print(dic)
dic.popitem()
print(dic)
print(user_info)
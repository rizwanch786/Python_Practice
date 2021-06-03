user_info = {
    'name' : 'Rizwan',
    'age' : 21,
    'fav_movies' : ['Tare Naam', 'Race'],
    'fav_tunes' : ['iphone', 'huawei']
}
# in keyword
# check if key exist in dictionary
if 'name' in user_info:
    print("Present")
else:
    print("Not Present")

# values method
# it give values in dictionary only
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# check if values exist in dictionary
if 'Rizwan' in user_info.values():
    print("Available")
else:
    print("Not Available")

# looping in dictionary
for i in user_info:
    print(i)
# it print key only but we want to print values in dictionary then we use values() method
for i in user_info.values():
    print(i)

#  keys method: it display keys in dictionary only
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# if we want to display values with the help of keys
for i in user_info:
    print(user_info[i])

# item() method: it give both key and its value in the form of tuple
user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))

#  if we want to get key and its values in seperate by using items() method in loop
for key, value in user_info.items():
    print(f"Key is {key} and value is {value}")
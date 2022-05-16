user_info = {
    'name': 'Rizwan',
    'age': 21,
    'fav_movies': ['Tare Naam', 'Race'],
    'fav_tunes': ['iphone', 'huawei'],
    'fav_songs': ['song1', 'song2'],
}


print(user_info)
# pop() method: it delete a selected item/data, it is like a list data type
popped = user_info.pop('fav_movies')
print(user_info)
print(popped)
print(type(popped))

# popitem() method: it remove data randomaly from the dictionary, it is like a tuple data type
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))
user = {}
name = input ("What is your name: ")
age = input ("What is your age: ")
fav_movies = input("your fav movies seperate by , : ").split(',')
fav_songs = input("your fav songs separate by , : ").split(',')
# enter values in dictionary
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
print (user)
for key, values in user:
    print (f"{key} : {values}")
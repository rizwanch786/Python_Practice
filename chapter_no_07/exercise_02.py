name = input ("What is your name: ")
age = input ("What is your age: ")
fav_movies = input("your fav movies seperate by , : ").split(',')
fav_songs = input("your fav songs separate by , : ").split(',')
user = {
    'name': name,
    'age': age,
    'fav_movies': fav_movies,
    'fav_songs': fav_songs,
}

print (user)
for key, values in user:
    print (f"{key} : {values}")
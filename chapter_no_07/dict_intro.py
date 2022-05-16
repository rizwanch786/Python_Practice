""" Q: Why we use dictionaries?
    A: Because of limitations of lists, lists are not enough to represent real data.
    example:
    user = ['Rizwan', 21,['tare name', 'Race'], ['iphone', 'huawei']]
    this list contains user name, age, fav movie, fav tunes.
    you can do this do not a good way to do this.
    
    Q: What are dictionaries?
    A: unordered collections of data in key : value pair
    """



    # How to create dictionaries?
    # # method_01
    # user = {'name':'Rizwan', 'age':21}
    # print (user)
    # print(type(user))
    # # method_02
    # user1 = dict(name = "rizwan", age  = 21)
    # print(user1)
    # print(type(user1))
    # # How to access data from dictionary?
    # # Note: there is no indexing because of unordered collections of data
    # print (user['name'])
    # print (user['age'])

    # # Which type of data a dictionary can store?
    # #  Anytype like: number, strings, lists and dictionaries

    # user_info = {
    #     'name':'Rizwan',
    #     'age':21,
    #     'fav_movies':['tare name', 'Race'],
    #     'fav_tunes':['iphone', 'huawei']
    # }
    # print (user_info)
    # print (user_info['fav_movies'])# how to add data to empty dictionary
userinfo2 = {'name': 'Chaudhary'}
print(userinfo2)
#  example
d = {'dog' : 'has a tail and goes woof!',
'cat' : 'says meow',
'mouse' : 'chased by cats'}
word = input ("Enter a word: ")
print (d[word])
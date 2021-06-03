# ZIP FUNCTION : It is used to combine more then one iterable's and convert it in to tuple's
user_id = ['user1', 'user2', 'user3']
names = ['Muhammad', 'Ali', 'Muhammad']
last_names = ['Rizwan', 'Raza', 'Khalique']
# zip(user_id, names)
# we convert it into list/dictionary and then display or it give an iterator object that is used to display values in for loop
print(list(zip(user_id,names)))
# output : [('user1', 'Muhammad'), ('user2', 'Ali'), ('user3', 'Muhammad')]
print (dict(zip(user_id,names)))
# output : {'user1': 'Muhammad', 'user2': 'Ali', 'user3': 'Muhammad'}
for i in zip(user_id,names):
    print(i)

# unpack lists
# *operator with zip
l = [(1,2),(3,4),(5,6),(7,8)]
# # l1 = [1,3,5,7]
# # l2 = [2,4,6,8]
# print (list(zip(*l)))
# output : [(1, 3, 5, 7), (2, 4, 6, 8)]
l1, l2 = list(zip(*l))
print (list(l1))
# output : [1, 3, 5, 7]
print(list(l2))
# output : [2, 4, 6, 8]
# # l1 = [1, 3, 5, 7]
# # l2 = [2, 4, 6, 8]
# using zip function compare both lists which list is greater
new_list = []
for pairs in zip(l1,l2):
    new_list.append(max(pairs))
print(new_list)
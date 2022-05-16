""" Insert Method:
Append method insert an item at the last of string 
but insert method is used to insert item in lost at a specific index of position.
"""

# fruits1.insert(1,"Grapes") # insert item at the mid 
# # fruits1.insert(2,"Grapes") # insert item at the last
# print (fruits1)

""" Extend Method:
It is used to add a list in other list.
"""
fruits2 = ["Grapes","Banana"]
# # fruits = fruits1 + fruits2
# # print(fruits)
# # But we want too add a list to other not concatenate then we use extend method
# fruits1.extend(fruits2)
# print(fruits1)

""" Append Method with Lists:
To join lists if append method is used instead of extends method then append method will append list in other list.
"""
fruits1 = ["Apple", "Mango", fruits2]
print(fruits1)

#  Extend() method is more better than Append() method
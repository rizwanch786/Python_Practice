# list
fruits = ['grapes', 'mango', 'apple']
fruits.sort()
print(fruits)
# or
print(sorted(fruits))

# tuple : tuple's are mutable therefor, we don't use sort method. if we want to use sort method then first convert it into a list.
# otherwise we use sorted function for sort the tuple the sorted function give sorted values into a list
fruits1 = ('grapes', 'mango', 'apple')
print(sorted(fruits1))

# sets: use sorted function and this function return a list
fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))

# complex data srtucture
bikes = [
    {'model':'Yahama 2015', 'price':80000},
    {'model': 'Suzuki 2002', 'price':45000},
    {'model':'Honda 2020', 'price':100000}
]
print (sorted(bikes,key=lambda b : b.get('price')))
# or
print(sorted(bikes,key=lambda b: b['price']))
# sort value's in reverse order
print(sorted(bikes,key=lambda b: b['price'],reverse = True))
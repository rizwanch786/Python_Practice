# MAX AND MIN FUNCTION
numbers = [1,2,4,6,7,4]
print (max(numbers))
# now we find maximum length of a string from a list
names = ['Rizwan', 'Ali', 'Khalique']
# for find maximum length we pass an function name or use lambda  funtion like:
print (max(names, key = lambda n : len(n)))
print (min(names, key = lambda n : len(n)))

student1 = [
    {'name' : 'Rizwan', 'score' : 90, 'age' : 21},
    {'name' : 'ALi', 'score' : 89, 'age' : 23},
    {'name' : 'Khalique', 'score' : 70, 'age' : 25}
]

# now we want to find maximum score from above list
print (max(student1, key = lambda items : items.get('score')))
# it give output like : {'name' : 'Rizwan', 'score' : 90, 'age' : 21}
# but we want to get name only then we use 
print (max(student1, key = lambda items : items.get('score')).get('name'))
# or
print (max(student1, key = lambda items : items.get('score'))['name'])
# it give output like : Rizwan

student2 = {
    'Rizwan' : {'score':99, 'age':21},
    'Ali' : {'score':79, 'age':23},
    'Khalique' : {'score':89, 'age':25}
}
# here we want the name according too maximum name
print(max(student2, key=lambda items : student2[items].get('score')))
print(max(student2, key=lambda items : student2[items].get('age')))
# if we don't use get mwthod then
print(max(student2, key=lambda items : student2[items]['score']))
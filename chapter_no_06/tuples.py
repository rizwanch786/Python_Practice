# Tuples : are store any type of data but it is immutable
example = (1,2,3,4,5,6,7,8,9,10)
print (example)
# looping in tuples
mixed = (1,4,5,3.42)
for i in mixed:
    print(i,end=" ")
#  tuples with single element
nums = (1) # it not a tuple it is a integer value for make it tuple we add comma (,) after element value
words = ('Hello',)
print(type(nums))
print(type(words))
# Tuples without pranthsis
fruits  = 'Apple', 'Banana', 'Mango'
print(fruits)
a,b,c = fruits
print (a)
print(b)
print(c)

# Lists in tuples
citys = ('Lahore',['Okara', 'Sahiwal'])
print(citys)
citys[1].pop()
print(citys)
citys[1].append('Depalpur')
print(citys)
# Function/Methods that are  used in tuples are: min(), max(), sum(), index(), slicing(), count(), len() only.
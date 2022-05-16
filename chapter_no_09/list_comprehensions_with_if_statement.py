numbers = list(range(1,11))
print (numbers)

even = [i for i in numbers if i%2 == 0]
print(even)

odd = [i for i in numbers if i%2 == 1]
print (odd)
# list comprehensions with if statement
even_number = [i for i in numbers if i%2 == 0]
print (even_number)
odd_number = [i for i in numbers if i%2 == 1]
print (odd_number)
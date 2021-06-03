# list comprehesion
squares = [i**2 for i in range (1,11)]
print(squares)

# generator comprehension
# simple replace [] into ()
generate_squares = (i**2 for i in range (1,11))
print(generate_squares)

for i in generate_squares:
    print(i)
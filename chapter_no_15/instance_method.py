# the first argument in every method is self (self mean object itself)

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return (f"{self.first_name} {self.last_name}")

    def is_above_18(self):
        return self.age > 18


# objects
p1 = Person("muhammad", "Rizwan", 21)
print(p1.full_name())
print(p1.is_above_18())
# or because we pass object as self therfore we access it like:
print(Person.full_name(p1))
print(Person.is_above_18(p1))

# we know that list is a class and below l is an list instance
# l = [1,2,3,4]
# we call many list methods with dot operator like
# l.append(10)
# here same concept we pass an class object itself as self like
# List.append(l,10)
# here l is the self object and 10 is the argument/ value that we want to store in the list
# print(l)
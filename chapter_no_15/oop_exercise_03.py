# give how many number of objects are created of that class 
class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1


# object's
p1 = Person("Rizwan", 21)
p2 = Person("Ali", 22)
p3 = Person("Khalique", 24)
print(Person.count)
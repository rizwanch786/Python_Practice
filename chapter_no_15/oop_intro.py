# how to create a class
# what is init method
# what are the attributes, instance variables
# how create class objects

class Person:
    # init is a constructor
    def __init__(self, name, age):
        # instance variables
        print("object created")
        self.name = name
        self.age = age

p1 = Person('Rizwan', 21)
print(p1.name)

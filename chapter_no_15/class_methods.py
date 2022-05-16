# Instance method: take first argument as object itself (self/ any name what you want). it is acccessed by object_name.method_name
# but
# Class_methods : take first argument as class itself (class_name/any name what you want). it is accessible by class_name.method_name.
# To differentiate instance/class methods we use @classmethod before class methods

# example
class Person:
    count = 0
    def __init__(self, name, age):
        Person.count += 1
        self.name = name
        self.age = age

    @classmethod
    def count_instance(cls):
        return f"you have created {cls.count} Instance in class {cls.__name__}"


# object's
p1 = Person("Rizwan", 21)
p2 = Person("Ali", 22)
p3 = Person("Khalique", 24)
print(Person.count_instance())
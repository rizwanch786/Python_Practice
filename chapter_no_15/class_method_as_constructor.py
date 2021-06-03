# we use class method as constructor like:

class Person:
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first,last,age) #here object is created
    

p1 = Person.from_string('M, Rizwan, 40')
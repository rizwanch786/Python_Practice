# Instance variables: every object of a class access different variables with different values.it access by object_name.variable_name
# Class variable's: every object in class share same name with same value of variables.it accessed by class_name.variable_name

class Circle:
    pi = 3.142
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_circumference(self):
        return 2*Circle.pi*self.radius

# object's
# if we want to change the value of pi then we direct access in the place like:
# Circle.pi = 0
c1 = Circle(4)
c2 = Circle(5)
print(c1.calculate_circumference())
print(c1.__dict__)

class Laptop:
    dicount_percentage = 10
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def calculate_discount(self):
        return (f"Total price after {self.dicount_percentage}% Discount is : {self.price - (self.dicount_percentage/100)*self.price}")

    
# objects
l1 = Laptop("HP", 'M3', 80000)
l2 = Laptop('Dell', 'Vestro', 29000)
print(l1.calculate_discount())
Laptop.dicount_percentage = 50
print(l1.calculate_discount())

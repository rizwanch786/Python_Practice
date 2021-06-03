# create a laptop class with attributes like: brand_name, model_name, price
# defind a function that calculate discount
# create two objects/ instance of your laptop class.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model_name = model
        self.price = price
        self.laptop = brand + " " + model

    def calculate_discount(self, d):
        return (f"Total price after {d}% discount : {self.price - ((d/100)*self.price)}")


# object's
l1 = Laptop('HP', 'M3', 29000)
l2 = Laptop('Dell', 'vestro', 80000)
print(l1.calculate_discount(40))
print(l2.calculate_discount(40))
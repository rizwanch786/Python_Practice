# create a laptop class with attributes like: brand_name, model_name, price
# create two objects/ instance of your laptop class.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand_name = brand
        self.model_name = model
        self.price = price
        self.laptop = brand + " " + model

# object's
l1 = Laptop('HP', 'M3', 29000)
l2 = Laptop('Dell', 'vestro', 80000)

print(f"Brand_Name : {l1.brand_name}, Model_name : {l1.model_name}, price : {l1.price}")

print(f"Brand_Name : {l2.brand_name}, Model_name : {l2.model_name}, price : {l2.price}")
print(l1.laptop)
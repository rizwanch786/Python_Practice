class Phone: #base class/ parent class
    def __init__(self, brand, model_name, price):
        self. brand = brand
        self.model_name = model_name
        self._price = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self, number):
        return f"calling {number}....."

# inherted class
class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two methods to access parent class constructor 
        Phone.__init__(self, brand, model_name, price)
        # or
        # super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera



# objects created
p1 = Phone("Nokia", "1600", 3600)
s1 = Smartphone("Sumsung", "A30", 30000, "4Gb", "64GB", "32MP")
print(f"{p1.full_name()} and price is {p1._price}")
print(f"{s1.full_name()} and price is {s1._price}")
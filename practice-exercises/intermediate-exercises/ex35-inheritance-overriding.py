class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def fuel_type(self):
        return "Petrol/Diesel"

class ElectricCar(Vehicle):
    # override the fuel_type method
    def fuel_type(self):
        return "Electricity"

my_tesla = ElectricCar("Tesla")
print(f"Brand: {my_tesla.brand}")
print(f"Fuel Type: {my_tesla.fuel_type()}")
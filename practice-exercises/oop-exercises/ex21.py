class Vehicle():
    def __init__(self, max_speed):
        self.max_speed = max_speed
    
    def describe(self):
        print(f"{type(self).__name__} max speed: {self.max_speed} km/h")
        # retrieves actual runtime class name 
        # makes the method usable without overriding it in each class

class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)

vehicles = [Bike(), Truck()]

for v in vehicles:
    v.describe()
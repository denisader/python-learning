class Vehicle():
    def __init__(self, name):
        self.name = name

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

class Bus(Vehicle):
    def seating_capacity(self): # overrides method to take no capacity argument
        super().seating_capacity(50)

bus = Bus("School Bus")
bus.seating_capacity()
# Python finds this version first and runs it instead of the parent's
class Vehicle():
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed}")

class Bus(Vehicle): # Bus inherits from Vehicle
    pass # Bus adds no new behavior
    # class is still fully functional because everything
    # comes from Vehicle

bus = Bus("School Bus", 120)
bus.display()
# Python first looks for display on the Bus instance
# then on the Bus class
# finally on Vehicle -> where it finds and executes method
# Method Resolution Order (MRO)
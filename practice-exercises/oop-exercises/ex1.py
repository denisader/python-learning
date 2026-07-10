class Vehicle():
    color = "White" # defined at class level so it belongs to all class instances
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    

def main():
    vehicle = Vehicle("Tesla Model S", 250, 18)
    print(f"Vehicle Name: {vehicle.name}, Color: {vehicle.color}, Speed: {vehicle.max_speed}, Mileage: {vehicle.mileage}")
    vehicle2 = Vehicle("BMW", 200, 10)
    print(f"Vehicle Name: {vehicle2.name}, Color: {vehicle2.color}, Speed: {vehicle2.max_speed}, Mileage: {vehicle2.mileage}")

    Vehicle.color = "Red"
    print(f"Vehicle Name: {vehicle.name}, Color: {vehicle.color}, Speed: {vehicle.max_speed}, Mileage: {vehicle.mileage}")
    print(f"Vehicle Name: {vehicle2.name}, Color: {vehicle2.color}, Speed: {vehicle2.max_speed}, Mileage: {vehicle2.mileage}")


if __name__ == '__main__':
    main()
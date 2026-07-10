class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)

def main():
    rect = Rectangle(10, 4)
    print(f"Area = {rect.area()}")
    print(f"Perimeter = {rect.perimeter()}")

if __name__ == "__main__":
    main()
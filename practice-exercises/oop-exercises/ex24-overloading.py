class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other): # Python calls this method automatically when + operator is used between 2 Vector objects
        # self is the left operand and other is the right one
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self): # defines the string representation of the object
        # used by print()
        return f"Vector({self.x}, {self.y})"
# same pattern applies to other operators such as __sub__, __mul__, __eq__

v1 = Vector(2, 3)
v2 = Vector(4, 1)

result = v1 + v2
print(result)
class Multiplier():
    def __init__(self, factor):
        self.factor = factor # stores multiplier value at construction time
        # object remembers its configuration between calls
        # this distinguishes callable objects from plain functions

    
    def __call__(self, value): # invoked whenever the object is called using parantheses
        return self.factor * value

triple = Multiplier(3)
penta = Multiplier(5)

print(triple(10))
print(penta(7))
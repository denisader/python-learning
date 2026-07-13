class PowerOfTwo():
    def __init__(self, max_exponent):
        self.max = max_exponent
        # remembers always where it is in the counting process
        self.n = 0
    
    # called when you start the for loop
    # it tells Python "I am an object that can be stepped through"
    def __iter__(self):
        return self

    # this is called on every iteration of the loop  
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
        else:
            # signal Python looks for to know the loop has finished
            # without this -> for loop would run forever
            raise StopIteration

for val in PowerOfTwo(3):
    print(val)
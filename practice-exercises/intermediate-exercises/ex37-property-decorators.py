class Student:
    def __init__(self, name):
       self.name = name
       self._score = 0

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("Score must be between 0 and 100.")

s = Student("Kevin")
try:
    s.score = 95
    print(f"{s.name}'s score: {s.score}")
    s.score = 105
except ValueError as e:
    print(f"Error: {e}")
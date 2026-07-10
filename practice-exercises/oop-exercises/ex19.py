class Media():
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def describe(self):
        return f"{self.title} - Rs.{self.price}"
    
class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    
    def describe(self):
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"

class Magazine(Media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self.frequency = frequency
    
    def describe(self):
        return f"Magazine: {self.title}, ({self.frequency}) - Rs.{self.price}"

items = [
    Book("Clean Code", 499, "Robert Martin"),
    Magazine("Wired", 150, "Monthly")
]

for item in items:
    print(item.describe())
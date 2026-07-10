class Animal():
    # init is not needed because we don't have any attributes to set
    # Python provides a defaul init automatically
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    # self is needed as a parameter because:
    # dog.speak() translates to Dog.speak(dog)
    # it automatically passes the instance as the first argument
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print("Dog says: ", dog.speak())
print("Cat says: ", cat.speak())
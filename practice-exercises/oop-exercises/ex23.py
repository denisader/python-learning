class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print("Is d an instance of Dog?", isinstance(d, Dog)) # because d is directly created from Dog class
print("Is d an instance of Animal?", isinstance(d, Animal)) # because Dog inherits from Animal
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal)) # Dog is defined with Animal as its parent
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog)) # parent doesn't inherit from the child
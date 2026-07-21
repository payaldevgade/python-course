# Parent Class

class Animal:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


# Child Class

class Dog(Animal):

    def __init__(self, name, breed):
        Animal.__init__(self, name)   # Calling Parent Constructor
        self.breed = breed

    def show(self):
        print("Breed:", self.breed)


# Object

d = Dog("Bruno", "German Shepherd")

d.display()
d.show()
# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create Object
d = Dog()

# Calling Methods
d.eat()     # Inherited from Parent
d.bark()    # Child's own method

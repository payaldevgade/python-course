# Grandparent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Parent Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Child Class
class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")

# Object
p = Puppy()

p.eat()    # From Animal
p.bark()   # From Dog
p.weep()   # From Puppy
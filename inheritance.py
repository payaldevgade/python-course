# Parent Class

class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# Child Class

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

# Object

d = Dog()

d.eat()      # Inherited method
d.sleep()    # Inherited method
d.bark()     # Child method

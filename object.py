# Class

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)

# Objects

s1 = Student("Rahul", 20)

s2 = Student("Priya", 19)

s1.display()

s2.display()
# USES __ __
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" hello how are you and your name is (self.tiger) "

    def __add__(self,other):
        return f" your sum of ages are {self.age + other.age}"
     

obj = Animal("Tiger",18)
obj2 = Animal("fish",16)

print(obj + obj2)
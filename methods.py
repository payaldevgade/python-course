class Student:
    name = " payal " # CLASS ATTRIBUTE

    def __init__(self,age):
        self.age = age #INSTANCE ATTRIBUTE

    def show(self): # INSTANCE METHOD
        print("How are you ,your age is {self.age}")

    @classmethod
    def hello(cls):
        print(F" how are you brother {cls.age}")

    @staticmethod
    def static():
        print("how are you bro ")

obj = Student(15)  

obj.static()



       
# PUBLIC ATTRIBUTES AND METHODS

class Student:
    a = " kee "

    def show(self):
        print(" hello i am a good person ")

class priya(Student):
    def show2(self):
        print(super().a)

obj = priya()
obj.show2()                
# PROTECTED ATTRIBUTES AND METHODS
# but in python we does not use this
# _ single underscore

class Student:
    _a = " kee "

    def _show(self):
        print(" hello i am a good person ")

class priya(Student):
    def show2(self):
        print(super()._a)

obj = priya()
obj.show2()                
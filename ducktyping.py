# DUCK TYPING
class Animal:
    def show(self):
        print(f" Hello i am showing")

class Human:
    def show(self):
        print(f" Hello i am also showing")

obj1 = Animal()
obj2 = Human()

obj1.show()
obj2.show()


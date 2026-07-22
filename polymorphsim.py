# METHOD OVER LOADING DOES NOT SUPPORT

class Animal:
    def show(self):
        print(f" Hello i am puppy")


# METHOD OVER RIDING SUPPORTS

class Human(Animal):
    def show(self):
        print(f" Hello i am anil")

obj = Human()

obj.show()


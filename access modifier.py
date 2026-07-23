class Demo:
    def __init__(self):
        self.name = " payal "       # PUBLIC
        self._age = 20              # PROTECTED 
        self.__salary = 900000      # PRIVATE

    def show(self):
        print(" inside the class :")
        print(" Public:" , self.name)
        print(" Protected:" , self._age)
        print(" Private:" , self.__salary)    

obj = Demo()

obj.show()
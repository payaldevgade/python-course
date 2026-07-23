from abc import ABC, abstractmethod

class Abstract(ABC):

    @abstractmethod
    def parameter(self):
        pass

    @abstractmethod
    def area(self):
        pass



class Square(Abstract):

    def __init__(self, side):
        self.side = side

    def parameter(self):
        print("Perimeter =", 4 * self.side)

    def area(self):
        print("Area =", self.side * self.side)


class Circle(Abstract):

    def __init__(self, radius):
        self.radius = radius

    def parameter(self):
        print("Circumference =", 2 * 3.14 * self.radius)

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)


obj = Circle(9)
obj.parameter()
obj.area()

obj2 = Square(12)
obj2.parameter()
obj2.area()
                      
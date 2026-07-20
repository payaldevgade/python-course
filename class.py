class Factory:
    a = 15 # ATTRIBUTE

    def hello(self):  # METHODS
        print("How are you")

    print(" Hello how are you i am getting initialized  ")

print(Factory().a)

Factory().hello()
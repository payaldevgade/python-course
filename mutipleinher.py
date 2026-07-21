# Parent Class 1
class Father:
    def money(self):
        print("Father has money")

# Parent Class 2
class Mother:
    def care(self):
        print("Mother takes care")

# Child Class
class Child(Father, Mother):
    def play(self):
        print("Child is playing")

# Object
c = Child()

c.money()   # From Father
c.care()    # From Mother
c.play()    # Child's own method
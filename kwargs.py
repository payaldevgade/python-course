# KEYWORD ARGUMENTS
# **
def information(**kwargs):
     print(" your information is\n\n")
     for i in kwargs:
          print(f" {i} : {kwargs[i]}")
     


information(name = "payal", age = 20, goal = "data scientist")


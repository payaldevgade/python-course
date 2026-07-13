import random

num = random.randint(1,10)

tries = 0

while True:
   
   guess = int(input("guess your number between 1 to 10:"))

   if num == guess:
      
      tries += 1

      print(f" you are the right you guessed the number is {tries} tries ")

      break
   
   elif num < guess:
      
      print(f" go a little lower number")

      tries += 1

   elif num > guess:
      
      print(f" go a little higher number")

      tries += 1

   else:
      
      tries += 1
      
      print(f" sorry you are wrong ")
         

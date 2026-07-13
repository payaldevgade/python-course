n = int(input("Check your number is perfect or not:"))

sum = 0

for i in range(1, n):

    if n% i == 0:
     
     sum = sum + i
        
    print(i) 

if sum == n:
    print(f" your number is perfect")

else:
    print(f" your number is not perfect")
       
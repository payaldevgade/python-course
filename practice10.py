n = int(input("Check your number is prime or not:"))
count = 0

for i in range(1, n+1):
    if n% i == 0:
     count = count + 1 

if count == 2:
    print(f" your number is prime")

else:
    print(f" your number is not prime")
       
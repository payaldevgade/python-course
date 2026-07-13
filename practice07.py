n = int(input("Enter a number:"))

even = 0

odd = 0

for i in range(1 , n+1):

    if i%2 == 0:


        even = even + i

    else:
        
        print(f"your even and odd sum are {even} , {odd}")

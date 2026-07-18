a = int(input("Enter a number"))

try:

    print(10 / a)

except ZeroDivisionError:
    
    print("sorry i cannot divide")
else:

    print("good there is no exception") 
finally:
    print(" i will run the code no matter what ")       

print("okayyy i have done division")    


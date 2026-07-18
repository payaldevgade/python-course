age = int(input(" enter your age:"))

try:

    if age < 10 or age > 18:
        raise ValueError(" your age must be between 10 and 18")
    
    else:

        print("welcome to the club")

except Exception  as e:
    print(f" an error occured as {e}")

print(" the club will start soon")            
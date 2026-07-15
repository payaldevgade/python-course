l = [20,40,50,39,59,30,99]

largest = l[0]

index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"your largest number is {largest} at index {index}:")
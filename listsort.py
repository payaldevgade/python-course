a = [24,25,26,27,28]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")

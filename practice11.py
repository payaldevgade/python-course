a = "naman"
b = ""
for i in range(len(a)-1, -1, -1):
    b = b + a[i]
if b == a:
    print(" your string is a palindrome")
else:
    print("your string is not a palindrome")
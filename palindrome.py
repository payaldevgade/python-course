a = int(input("enter a number"))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10

    a = a // 10
if copy == rev:
    print(f" palindrome number ")
else:
    print(f" not a palindrome number ")

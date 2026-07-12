year = int(input("tell your year:" ))
if year %100 == 0 or year%400 == 0:
    print("century leap year")
elif year%100 != 0 or year%4 == 0:
    print("leap year")
else:
    print("its a normal year")
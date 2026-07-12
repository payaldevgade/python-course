t = int(input("Tell your Temperture:"))
if t < 0:
    print(f"Freezing Cold")
elif t >= 0 and t < 10:
    print(f"Very Cold")
elif t >= 10 and t < 20:
    print(f"Cold")
elif t >= 20 and t < 30:
    print(f"Plesant")
elif t >= 30 and t < 40:
    print(f"Hot")

else:
    print("Temperture is Very Hot")

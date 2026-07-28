def decorate(func):
    def wrapper(a,b):
        print(" The addition to your number are ")
        func(a,b)
        print(" Thank you i hope you liked it")
    return wrapper


@decorate

def addition(a,b):
    print(f" your total is {a+b}")

addition(29 ,67)    


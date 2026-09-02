def decorate(func):
    
    def wrapper(*args, **kwargs):
        print(" The addition to your number are ")
        func(*args, **kwargs)
        print(" Thank you i hope you liked it")
        
    return wrapper


@decorate

def addition(a,b):
    print(f" your total is {a+b}")

addition(29 ,67)    


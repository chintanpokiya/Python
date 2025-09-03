def error_handling():
    try:
        x=int(input("Enter 1st Number :- "))
        y=int(input("Enter 2nd Number :- "))
        print(x/y)
    except:
        print("Something bad happened..!!!")
error_handling()

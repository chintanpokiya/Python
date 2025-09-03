while True:
    try:
        x = int(input("please enter a number:- "))
        break
    except ValueError as v:
        print("OOPS! That was no valid number ..!!! Try Again....")
        print(v)

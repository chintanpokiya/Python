def add(a,b):
    print("Sum of a=",a,"and b=",b," IS :- ",a+b)

def sub():
    a=20
    b=10
    return a-b

def main():
    print("Welcome to LJKU PORTAL!!")
    print("Select one of the following for arithmetic operation")
    while(True):
        print("1. Addition")
        print("2. Addition")
        print("3. Exit")
        print("Enter the choice number from above")
        choice = int(input())
        if choice == 1:
            print("You have chosen addition operation..!!")
            add(10,20)
            break
        elif choice == 2:
            print("You have chosen Subtraction..!!")
            rea=sub()
            print("Subtraction",rea)
            break
        elif choice == 3:
            break
        else:
            print("You have entered as invalid choice..!!")

if __name__ == '__main__':
    main()
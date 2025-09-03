import os 

def create_dir():
    dir = input("Enter Directory Name :- ")
    if os.path.exists(dir):
        print("Directory Already Exists..!!")
    else:
        os.mkdir(dir)

def change_dir():
    d_name = input("Enter Directory Name to Change :- ")
    os.chdir(d_name)

def currentwork_dir():
    print(os.getcwd())

def rename_dir():
    

def main():
    while(True):
        print("---------------------- Welcome MENU DRIVEN ----------------------")
        print("1. Create Diretory")
        print("2. Change Directory")
        print("3. Rename Directory")
        print("4. Remove Directory")
        print("5. Current Working Directory")
        print("6.Exit")
        print("-----------------------------------------------------------------")
        choice = input("Enter Your Choice :- ")

        if choice == '1':
            create_dir()
        
        elif choice == '2':
            change_dir()

        elif choice == '3':
            rename_dir()
            
        elif choice == '4':
            remove_dir()
            
        elif choice == '5':
            currentwork_dir()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid Choice Plz Try Again..!!")

if __name__ == "__main__":
    main()

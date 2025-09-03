import os 

#file path
file_path = 'records.txt'

#function to read all records
def read_records():
    if not os.path.exists(file_path):
        print("No records found..!!!")
        return

    with open(file_path,'r') as file:
        records = file.readlines()
        if records:
            for record in records:
                    print(record.strip())
            else:
                print("No records found..!!")

#function to write a new record
def write_records(record_id,name,s1,s2,s3):
    with open(file_path,'a') as file:
        file.write(f"{record_id},{name},{s1},{s2},{s3} \n")
    print(f"Record {record_id} added..!!")

#function to update a record

def update_record()

#function to search a record

def search_record(filename,search_term):
    try:
        with open(file_path , 'r') as file:
            found = False
            for line in file:
                if search_term in line:
                    # rec = line.strip().split(',')
                    # if rec[0] == search_term:
                    print("Record Found :- ",line.strip().split(','))                      
                    print("Record Found :- "+line.strip())
                    found = True
            if not found:
                print(f'no record found for :- "{search_term}".')
    except FileNotFoundError:
        print("File Not Found..!!")

#main function for demonstration

def main():
    while(True):
        print("---------------------- Welcome MENU DRIVEN ----------------------")
        print("1.Read Records")
        print("2.Write a new Record")
        print("3.Update a Record")
        print("4.Delete a Record")
        print("5.Search a Record")
        print("6.Exit")
        print("-----------------------------------------------------------------")
        choice = input("Enter Your Choice :- ")

        if choice == '1':
            read_records()
        
        elif choice == '2':
            record_id = input("Enter id :- ")
            name = input("Enter Name :- ")
            s1 = input("Enter Sub1 Marks :- ")
            s2 = input("Enter Sub2 Marks :- ")
            s3 = input("Enter Sub3 Marks :- ")
            write_records(record_id,name,s1,s2,s3)

        elif choice == '3':
            new_record_id = input("Enter id to update :- ")
            new_name = input("Enter new Name :- ")
            new_s1 = input("Enter new Sub1 Marks :- ")
            new_s2 = input("Enter new Sub2 Marks :- ")
            new_s3 = input("Enter new Sub3 Marks :- ")
            update_record(new_record_id,new_name,new_s1,new_s2,new_s3)

        elif choice == '4':
            record_id = input("Enter ID to Delete :- ")
            delete_record(record_id)

        elif choice == '5':
            search_term = input("Enter Record Id Or Name :- ")
            search_record(file_path,search_term)            

        elif choice == '6':
            break
        
        else:
            print("Invalid Choice Plz Try Again..!!")

if __name__ == "__main__":
    main()

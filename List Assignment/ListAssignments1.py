"""
Write a MENU Driven Program for Following
1. Create Empty List with List() and and range function
2. Display List
3. Count No of Elements in List
4  Create another list OddList and EvenList
5. Display ODD and EVEN LISt ELEMENT
6. Check entered Element is In List Exist or Not
7. Print elements of List which is devided  By 5
8. Print the sum of element List
9. Create Two List of any element and copyBoth elements to Third
   List
10. Count no of int element , float element and string
    form list
0. Exit
 Employee ID :2091
 Author: V.U.Ingle
 Date o Creation :---
 TIme OF Creation :---

"""

def create_list():
    return list(range(int(input("Enter start of range: ")), int(input("Enter end of range: "))))

def display_list(lst):
    print("List elements are:", lst)

def count_elements(lst):
    print("Number of elements in list:", len(lst))

def create_odd_even_lists(lst):
    odd_list = [x for x in lst if x % 2 != 0]
    
    even_list = [x for x in lst if x % 2 == 0]
    return odd_list, even_list

def display_odd_even_lists(odd_list, even_list):
    print("Odd List:", odd_list)
    print("Even List:", even_list)

def check_element_in_list(lst):
    elem = input("Enter element to check: ")
    if elem.isdigit():
        elem = int(elem)
    elif elem.replace('.', '', 1).isdigit():
        elem = float(elem)
    if elem in lst:
        print(f"{elem} is in the list.")
    else:
        print(f"{elem} is not in the list.")

def print_divisible_by_5(lst):
    divisible_by_5 = [x for x in lst if isinstance(x, int) and x % 5 == 0]
    print("Elements divisible by 5:", divisible_by_5)

def sum_of_elements(lst):
    sum_elements = sum([x for x in lst if isinstance(x, (int, float))])
    print("Sum of elements in the list:", sum_elements)

def create_and_copy_lists():
    list1 = input("Enter elements for first list (comma-separated): ").split(',')
    list2 = input("Enter elements for second list (comma-separated): ").split(',')
    list3 = list1 + list2
    print("Combined list:", list3)

def count_element_types(lst):
    int_count = len([x for x in lst if isinstance(x, int)])
    float_count = len([x for x in lst if isinstance(x, float)])
    str_count = len([x for x in lst if isinstance(x, str)])
    print(f"Number of integer elements: {int_count}")
    print(f"Number of float elements: {float_count}")
    print(f"Number of string elements: {str_count}")

def menu():
    lst = []
    while True:
        print("\nMenu:")
        print("1. Create Empty List with List() and range function") 
        print("2. Display List")
        print("3. Count No of Elements in List")
        print("4. Create another list OddList and EvenList")
        print("5. Display ODD and EVEN LISt ELEMENT")
        print("6. Check entered Element is In List Exist or Not ")
        print("7. Print elements of List which is divided By 5")
        print("8. Print the sum of element List")
        print("9. Create Two Lists and copy both elements to Third List")
        print("10. Count no of int element, float element and string in list")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            lst = create_list()
        elif choice == 2:
            display_list(lst)
        elif choice == 3:
            count_elements(lst)
        elif choice == 4:
            odd_list, even_list = create_odd_even_lists(lst)
        elif choice == 5:
            display_odd_even_lists(odd_list, even_list)
            o,e=display_odd_even_lists(odd_list, even_list)
            
        elif choice == 6:
            check_element_in_list(lst)
        elif choice == 7:
            print_divisible_by_5(lst)
        elif choice == 8:
            sum_of_elements(lst)
        elif choice == 9:
            create_and_copy_lists()
        elif choice == 10:
            count_element_types(lst)
        elif choice == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()

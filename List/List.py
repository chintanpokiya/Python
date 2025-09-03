"""Definition : List
Author : Neelkanth Parekh
Date of creation : 7/8/2024
Time : 12:01 PM
Time of creation : Wednesday"""

"""List :- array contain same data type
        list represents a group of elements like array
        lists are very similar to array there is major difference an array can store only one type of elements whereas a list can store different type of elements.
        lists are mutuable so we can modify its element
        a list can store different types of elements which can be modified.
        lists are dynamic which means size is not fixed
        lists are represented by square bracket [].
        Ex :- a = [12,20,-40,21.3,'Neelkanth']
        Similar data type also supported

        Create a list
        a list is similar to an array that consists of a group of elements or items.
        syntax :- list_name[element1,element2,.......]
        Ex :- a = [12,20,-40,21.3,'Neelkanth']

        Empty list

        syntax = list_name = []
        Ex :- a=[]

        Index :- An index represent the position number of an lists element. The index start with from 0 on words ..........

        Access the elements

        Deletion :- del statement is used to delete an element of list or we can delete entire list using del statement 
        a=[10,20,-24,21.3,"Neelkanth"] 


        append() :- this method is used to add an element and add to this after....
        syntax :- 

        insert() :- this method to used to insert an element in particular position of the existing list.
        syntax:- 
                list_name insert(position_number,new_element)

        pop() :- this is used to remove the last element from the existing list.
        syntax :- 
                list_name.pop()
"""

# 1. create empty list...

# a = []
# print(a)
# print("The type of a is :- ",type(a))

# 2. create the list and access the element using index and without index

# a=[10,20,-12,13,14,"Neelkanth Parekh"]
# print(a)
# print("The type of a is :- ",type(a))

#without index 

# for l in a:
#     print(l)

#with index

# for i in range(len(a)):
#     print(a[i])

# 3. Accessing using while loop

# a=[10,20,-12,13,14,"Neelkanth Parekh"]
# print(a)
# print("The type of a is :- ",type(a))

# using while loop

# l=0
# while l<len(a):
#     print(a[l])
#     l=l+1

# 4. Deletetion

#DELETE ELEMENT WITH INDEX 

# a=[10,20,-12,13,14,"Neelkanth Parekh"]

# print(a)

#with index

# del a[2]
# print(a)

# delete all elements from the list 

# del a
# print(a)
# print(type(a))

# 5. append ()

# a=[]
# n=int(input("Enter Number of elements :- "))
# for i in range(n):
#     a.append(int(input("Enter Element")))

# print("list")
# for element in a:
#     print(element)

# 6. insert ()

# a=[]
# n=int(input("Enter Number of elements :- "))
# for i in range(n):
#     a.append(int(input("Enter Element")))

# print("list",end=" ")

# for element in a:
#     print(element,end=" ")

# print()
# ele=int(input("Enter Number of elements :- "))
# pos=int(input("Enter Number of elements :- "))

# a.insert(int(input("Enter Element")))

# print(a)


# 7. pop

# a=[]
# n=int(input("Enter Number of elements :- "))
# for i in range(n):
#     a.append(int(input("Enter Element")))

# print("list",end=" ")

# for element in a:
#     print(element,end=" ")

# print()
# ele=int(input("Enter Number of elements :- "))
# pos=int(input("Enter Number of elements :- "))

# a.pop()

# print(a)


# 8. pop with parameter

# a=[]
# n=int(input("Enter Number of elements :- "))
# for i in range(n):
#     a.append(int(input("Enter Element")))

# print("list",end=" ")

# for element in a:
#     print(element,end=" ")

# print()
# ele=int(input("Enter Number of elements :- "))
# pos=int(input("Enter Number of elements :- "))

# a.pop("index")

# print(a)

# 9. remove element 

# a=[]
# n=int(input("Enter length :- "))
# for i in range(n):
#     a.append(int(input("Enter Elements :- ")))

# print("list :- ",end=" ")

# for element in a:
#     print(element,end=" ")

# print()
# ele=int(input("enter the element to remove : - "))
# a.remove(ele)

# print(a)

# 10. index element 

# a=[10,20,30,"Neelkanth"]

# print(a.index(20))

#11. reverse element 

# a=[10,20,30,40,50]
# a.reverse()
# print(a)

# for i in range(-len(a),0,1):
#     print(a[i],end=" ")

# 12. extend()

# a=[10,20,30,40,50,"Neelkanth"]
# b=[100,200,300]

# print("Before Extend :- ",a)

# a.extend(b)

# print("After Extend :- ",a)

# for element in a:
#     print(element)
# print(a)

# 13. sort & clear

# a=[12,34,32,22,10]
# print(a)
# a.sort()
# print(a)

# a=[12,34,32,22,10]
# print(a)
# a.clear()
# print(a)
# print(type(a))

# 14. slicing 

# x = [101,102,103,104,105,106,107]
# print("Original List :- ")
# n = len(x)
# for i in range(n):
#     print(i, "=",x[i])
# print()

# print("From 1st position to 4th position :- ")
# a = x[1:5]
# for i in a:
#     print(i)
# print()


# print("From 0th position to last position :- ")
# b = x[0:]
# for i in b:
#     print(i)
# print()

# print("From 0th position to 4th position :- ")
# c = x[:5]
# for i in c:
#     print(i)
# print()

# print("Last 4 elements :- ")
# d = x[-4:]
# for i in d:
#     print(i)
# print()

# print("From 0th position to 6th position stride 2:- ")
# e = x[0:7:2]
# for i in e:
#     print(i)
# print()

# print("Last 5 elements with [-5(-3)]=2 elements towards right")
# f = x[-5:-3]
# for i in f:
#     print(i)
# print()

# 15. list concatenation

# a="Neelkanth"
# b="Parekh"
# c=a+b
# print(c)
# print(type(c))

# 16. repetition of list

# b=[1,2,3]
# result = b*3
# print(result)

# 17. aliasing 

# a=[10,20,30,40,50]
# b=a
# print("A:- ",a)
# print("B:- ",b)

# print()
# print("Modifying A :- ")
# a[1] = 55
# print("A:- ",a)
# print("B:- ",b)

# print()
# print("Modifying B :- ")
# a[2] = 66
# print("A:- ",a)
# print("B:- ",b)


# 18. copy list

# a=[10,20,30,40,50]
# b=a.copy()
# print("A:- ",a)
# print("B:- ",b)
# print("A:- ",id(a))
# print("B:- ",id(b))

# print()
# print("Modifying A :- ")
# a[1] = 55
# print("A:- ",a)
# print("B:- ",b)

# print()
# print("Modifying B :- ")
# a[2] = 66
# print("A:- ",a)
# print("B:- ",b)


# cloning 

# a=[10,20,30,40,50]
# b=a[:]
# print("A:- ",a)
# print("B:- ",b)
# print("A:- ",id(a))
# print("B:- ",id(b))

# print()
# print("Modifying A :- ")
# a[1] = 55
# print("A:- ",a)
# print("B:- ",b)

# print()
# print("Modifying B :- ")
# a[2] = 66
# print("A:- ",a)
# print("B:- ",b)
"""Definition : Nested list , Index
Author : Neelkanth Parekh
Date of creation : 9/8/2024
Time : 9:12 AM
Er No : 22004500210151
Time of creation : Friday"""

'''
Nested List :- A list within another list is called a nested list or nesting of a list.

Ex:- 
    a = [10,20,30,[50,60]]
    
    b = [50,60]
    a = [10,20,30,b]
    
    a = [ [10,20,30],[40,50,60] ]
    a = [ [10,20,30],
        [40,50,60] ]


Index :- 

a = [10,20,30,[50,60]]

b = [50,60]
a = [10,20,30,b]

10 20 30 50 60
== == == =======
0   1  2    3

  a = [ [10,20,30],[40,50,60] ]
    a = [ [10,20,30],
        [40,50,60] ]


Accessing nested list :- 

a = [10,20,30,[50,60]]

b = [50,60]
a = [10,20,30,b]

10 20 30 50 60
== == == =======
0   1  2    3

  a = [ [10,20,30],[40,50,60] ]
    a = [ [10,20,30],
        [40,50,60] ]

print(a[0])
print(a[1])
print(a[2])
print(a[3][0])


Modifying nested list :- 
a = [10,20,30,[50,60]]

b = [50,60]
a = [10,20,30,b]


'''


#nested list 

#example 1
# a = [10,20,30,[50,60]]
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[3][0])
# print(a[3][1])

#example 2

# b=[50,60]
# a=[10,20,30,b]
# print("A :- ",a)
# print("B :- ",b)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[3][0])
# print(a[3][1])


#nested list 

# a = [[10,20,30],[40,50,60]]
# print("A :- ",a)
# print("a[0]:- ",a[0])
# print("a[1]:- ",a[1])
# print()
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])


#nested list - modification

# a = [10,20,30,[50,60]]

# print("Before Modification A :- ",a)
# print()
# a[1]=100
# a[3][0]=5
# print("Before Modification A :- ",a)

# a = [[10,20,30],[40,50,60]]

# print("Before Modification A :- ",a)
# print()
# a[0][1]=2
# a[1][2]=6
# print("After Modification A :- ",a)

#accessing nested list using for loop (nested loop - for loop with index)


# a = [[10,20,30],[40,50,60]]
# n = len(a)

#without index

# for r in a:
#   for c in r:
#     print(c)
#   print()

  
# #with index 
# for i in range(n):
#   if type(a[i]) is list:
#     if len(a[i])>1:
#       m = len(a[i])
#       for j in range(m):
#         print(i,j, a[i][j])
#   else:
#     print(i,a[i])


#nested list using while loop

# a = [[10,20,30],[40,50,60]]
# n = len(a)

#using while loop

# a=[[10,20,30],[40,50,60]]
# n=len(a)

# i = 0
# while i < n:
#   j = 0
#   while j < len(a[i]):
#     print(a[i][j])
#     j+=1
#   i+=1

#list 

a=list()
print(a)
print(type(a))

#creating list using list function and range function 

b=list(range(0,5))
print(b)
print(type(b))
'''
Name : Parekh Neelkanth
Div : c 
Er no : 22004500210151
Topic : Dictionary Assignment
Time : 1:21
Day : Wednesday
Date : 14/08/2024
'''

# a = {1:25,2:21,3:23}
# asc = list()
# desc = list()
# print(a)

# #Ascending order:-

# asc=sorted(a.values())
# print("Ascending order :- ",asc)

# #Descending order

# desc=sorted(a.values(),reverse=True)
# print("Descending order :- ",desc)


#using bubble sort

# def bubble_sort(arr,ascending=True):
#     n = len(arr)
#     for i in range(n):
#         #track if any swaps were made
#         swapped = False
#         for j in range(0,n-i-1):
#             # check if we need to swap elements
#             if(ascending and arr[j] > arr[j+1])or(not ascending and arr[j] < arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#             swapped = True
#             # if no swaps were made the array is sorted
#             if not swapped:
#                 break

# #original dictionary
# original_dict = {1:25,2:21,3:23}

# #extract the values from the dictionary
# values = list(original_dict.values())

# #sort values in ascending order
# bubble_sort(values,ascending=True)
# print("Ascending Order :- ",values)

# #Sort values in descending order
# bubble_sort(values,ascending=False)
# print("Descending order :- ",values)



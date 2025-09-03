# """
# *
# **
# ***
# ****
# *****
# """
print(__doc__)
# for i in range(5):
#     for j in range(1,i+1):
#         print("1",end=" ")
#         print("1 ",end=" ")
#     print("\n")

# x=0
# for i in range(1,6):
#     for j in range(0,i+1):
        # print(j,end=" ")
        # print(x:=x+1,end=" ")
    #     print(i*j,end=" ")
    #     # print("1 ",end=" ")
    # print("\n")

# for i in range(5):
#     for j in range(0,i-1):
#         # print("*",end="")
#         print("*",end=" ")
#     print("\n")





# rows = 5
# k = 2 * rows - 2    

# for i in range(0, rows):    

#     for j in range(0, k):    
#         print(end=" ")    

#     k = k - 1    

#     for j in range(0, i + 1):    
#         print("* ", end="")    
#     print("")    


# k = rows - 2    

# for i in range(rows, -1, -1):    

#     for j in range(k, 0, -1):    
#         print(end=" ")    

#     k = k + 1    

#     for j in range(0, i + 1):    
#         print("* ", end="")    
#     print("")    


rows = 5


for i in range(1, rows+1):  
    num = 1
    
    
    for j in range(rows,0,-1):  
      if j > i:
        print(" ", end=" ") 
      else:
        print(num, end=" ")
        num += 1
  
    
    print()

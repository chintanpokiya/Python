'''write a one python program to accept no from the users and 
check whether entered number is find out max number
'''

#Accept number from the user
a = int(input("Enter Number : "))
b = int(input("Enter Number : "))

#Check whether no is max,min or same
if(a>b):
    print("A No is Max")
elif(a<b):
    print("B No is Max")
else:
    print("Both are same")

print("End of program")
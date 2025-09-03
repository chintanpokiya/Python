'''write a one python program to accept no from the users and 
check whether entered as
binary BIN(NO)
hexa   HEX(NO)
octal  OCT(NO)
'''

#Accept number from the user
a = int(input("Enter Number : "))

#Check whether no is oct,bin,hexa

bin=bin(a)
print("Decimal to Binary",bin)

hex=hex(a)
print("Decimal to Hexa",hex)

oct=oct(a)
print("Decimal to Oct",oct)
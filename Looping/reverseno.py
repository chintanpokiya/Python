#write a program in python except numbers from the users and display original nos and reverse it (Entered No) using while loop and cheok entered no is palindrome or not....

num=int(input("Enter Number :- "))
print(num)
temp = num
reverse = 0
while(temp > 0):
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp//10
if num == reverse:
    print("Entered no :- ",num,"Reverse No :- ",reverse)
    print("Entered No :- ",num,"is palindrome")
else:
    print("Entered NO is not palindrome")
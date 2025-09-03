"""Definition : To create a string creation
Author : Neelkanth Parekh
Date of creation : 2/8/2024
Time of creation : Friday"""

str1 = 'Neelkanth Parekh' #using single quotes
print(str1)

str2 = "Neelkanth Parekh" #using double quotes
print(str2)

str3 = '''Neelkanth
        Parekh 
        '''

print(str3) #display string of str3 for single quotes

str4 = """Neelkanth 
        Parekh
        """
print(str4) # Display string of str4 for multi line

str5 ="""Neelkanth \n Parekh """
print(str5) #Display string of str5 for \n..

rstr6 = r"""Neelkanth \n parekh"""
print(rstr6) #Display string of rstsr6 ignore for row string.




#memory address


str1="Neelkanth"
str2="Neelkanth"
str3="Parekh"
str4 = str3
print("str1=",str1, id(str1))
print("str2=",str2, id(str2))
print("str3=",str3, id(str3))
print("str4=",str4, id(str4))



str1="Neelkanth"
print("str1= ",id(str1))
str1="parekh"
print("str1= ",id(str1))



str1="Neelkanth Parekh"
n = len(str1)
print(n)


str1="Neel"

print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])


str1 = "Neelkanth"
for c in str1:
    print(c)


str1 = "neelkanth"
i = 0
while i < len(str1):
    print(str1[i])
    i+=1

# str1="neelkanth"
# str1[4] = "i"
# for c in str1:
#     print(c)


#syntax of slicing

# new_string_name = string_name[start:stop:stepsize]



str1="Neelkanth"
str2="Neelkanth"
str3="Parekh"
str4 = "A"
str5 = "b"
result1 = str1 == str2
result2 = str1 == str3
result3 = str4 < str5
print(result1)
print(result2)
print(result3)
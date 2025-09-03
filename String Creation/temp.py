"""Definition : To create a string creation
Author : Neelkanth Parekh
Date of creation : 3/8/2024
Time of creation : Saturday"""

print("***********UPPER FUNCTION***********")
name = "corepython"
str1 = name.upper()
print(name)
print(str1)

print("***********LOWER FUNCTION***********")
name = "COREPYTHON"
str1 = name.lower()
print(name)
print(str1)

print("***********SWAPCASE FUNCTION***********")
name = "corepython"
str1 = name.swapcase()
print(name)
print(str1)

print("***********TITLE FUNCTION***********")
name = "hello corepython how are you"
str1 = name.title()
print(name)
print(str1)

print("***********ISUPPER FUNCTION***********")
name = "COREPYTHON"
str1 = name.isupper()
print(name)
print(str1)

print("***********ISLOWER FUNCTION***********")
name = "corepython"
str1 = name.islower()
print(name)
print(str1)

print("***********ISTITLE FUNCTION***********")
name = "Hello Corepython How Are You"
str1 = name.istitle()
print(name)
print(str1)

print("***********ISDIGIT FUNCTION***********")
name = "342343"
str1 = name.isdigit()
print(name)
print(str1)

print("***********ISALPHA FUNCTION***********")
name = "COREpython"
str1 = name.isalpha()
print(name)
print(str1)

print("***********ISALNUM FUNCTION***********")
name = "COREpython2343"
str1 = name.isalnum()
print(name)
print(str1)

print("***********ISSPACE FUNCTION***********")
name = "  "
str1 = name.isspace()
print(name)
print(str1)

print("***********LSTRIP FUNCTION***********")
name = "    CorePython"
str1 = name.lstrip()
print(name)
print(str1)

print("***********RSTRIP FUNCTION***********")
name = "CorePython  "
str1 = name.rstrip()
print(name)
print(str1)

print("***********SSTRIP FUNCTION***********")
name = "    CorePython  "
str1 = name.strip()
print(name)
print(str1)

print("***********REPLACE FUNCTION***********")
name = "CorePython"
old = "Core"
new = "New"
str1 = name.replace(old , new)
print(name)
print(str1)

print("***********SPLIT FUNCTION***********")
name = "Hello-how-are-you"
print("Datatype of name = ",type(name))
str1 = name.split('-')
print(name)
print(str1)
print("Datatype of str1 = ",type(str1))


print("***********JOIN FUNCTION***********")
name = ('Hello','How','Are','You')
print("Datatype of name = ",type(name))
str1 = "_".join(name)
print(name)
print("Datatype of str1 = ",type(str1))

print("***********STARTSWITH FUNCTION***********")
name = "Hi How are you"
str1 = name.startswith('Hi')
print(name)
print(str1)

print("***********ENDSWITH FUNCTION***********")
name = "Thank You Bye"
str1 = name.endswith('Bye')
print(name)
print(str1)



# str1 = """This is an example of count the characters count the number of upper character and lower character and findout the total no of character for the following string """

# 0. Length of String
# 1. Count the nos of capital letter
# 2. Small letter
# 3. Digit letter
# 4. Alpha letter
# 5. Alphanumeric letter
# 6. Space letter
# 7. Word letter
# 8. Special letter
# 9. lines

print(__doc__)

str1 = "This is an example of count the characters count the number of upper character and lower character and findout the total no of character for the following string"

length=len(str1)
cap = 0 
for ch in str1:
    if ch.isupper():
        cl = cl+1
    elif ch.islower():
        sl = sl+1
    elif ch.isdigit():
        dl = dl+1
    elif ch.isalpha():
        alpha = alpha+1
    elif ch.isalnum():
        alnum = alnum+1
    elif ch.isspace():
        space = space+1
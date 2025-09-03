import random
import array

# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 12

#declare arrays of the character that we need in out password
#represented as chars to enable easy string conctenation

"""
Password contain
digit
character - 1 char must B in capital
specialcharacter 1
Len 12
"""


DIGITS = ['0','1','2','3','4','5','6','7','8','9']

LOCASE_CHARACTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_CHARACTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SPECIAL_CHARACTERS = ['!','@','#','$','%','^','&','*','=',':','?','.','/','|','~','(',')','<']
                    

COMBINED_LIST = DIGITS + UPPER_CHARACTERS + LOCASE_CHARACTERS + SPECIAL_CHARACTERS
print(COMBINED_LIST)
password=""
for i in range(0,12):
    password=password+random.choice(COMBINED_LIST)
print(password)
d = random.choice

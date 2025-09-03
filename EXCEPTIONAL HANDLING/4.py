'''
Write a program write 1 to 100 into file and read the this nos from the file and display only even nos and
 that opens a file and handles 
'''

filename="number.txt"

with open(filename,"w") as file:
    for i in range(1,101):
        file.write(f'{i}\n')

try:
    with open(filename,"r") as file:
        data=file.readlines()
    for i in data:
            if int(i) % 2 == 0:
                print(i)
except FileNotFoundError as F:
    print(F)

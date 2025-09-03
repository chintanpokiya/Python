#variable_length arguments
#example 1
def add(*num):
    print(type(num))
    z=num[0]+num[1]+num[2]
    print("Addition :- ",z)

add(5,2,4)

#example 2
def add(x,y):
    z=x+y
    print("Addition :- ",z)

add(5,2)

#example 3
def add(x,*num):
    # print(type(num))
    z=x+num[0]+num[1]
    print("Addition :- ",z)

add(5,2,4)
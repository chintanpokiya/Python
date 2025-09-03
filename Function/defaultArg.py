#default arguments
#example 1
def show(name,age):
    print(f"Name : {name} Age : {age} ")

show(name="Neelkanth Parekh",age=20)

#example 2
def show(name,age=20):
    print(f"Name : {name} Age : {age} ")

show(name="Neelkanth Parekh")

#example 3
def show(name,age=20):
    print(f"Name : {name} Age : {age} ")

show(name="Neelkanth Parekh",age=20)

#example 4 it will give error
'''def show(name,age=20):
    print(f"Name : {name} Age : {age} ")

show(name="Neelkanth Parekh",age=20,rollno=101)'''
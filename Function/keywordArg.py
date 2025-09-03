#keyword arguments
#example 1
def show(name,age):
    print(f"name:-{name} age:{age}")

show(name="Neelkanth",age=20)

#example 2
def show(name,age):
    print(f"name:-{name} age:{age}")

show(age=20,name="Neelkanth")


#example 3 it will show error
'''def show(name,age):
    print(f"name:-{name} age:{age}")

show(age=20,name="Neelkanth",rollno=101)'''
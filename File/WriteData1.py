# Writing data with w mode example 1 
f=open('student.txt',mode="w")
f.write("Hello")
f.write("Neelkanth")
f.write("Parekh")
f.write("How are You ??")
f.close()
print('Success')
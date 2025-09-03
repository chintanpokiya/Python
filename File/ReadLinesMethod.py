# Reading data with r mode
f=open('student.txt',mode='r')
data = f.readlines()
print(data)
for i in data:
    # print(i,end='')
    print(i)
f.close()

print("=============================================")

f=open('student.txt',mode='r')
data = f.read()
cl=0
for i in data:
    if i == 'L':
        cl=cl+1
        # print(i)
f.close()
print("No of CL in the file ",cl)
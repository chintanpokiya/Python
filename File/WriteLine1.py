#writing data with w mode

f=open('student.txt',mode='w')
lst = ['Neelkanth','Mukesh','Jaimin','Sachin','Devraj']
f.writelines(lst)
f.close()
print('Success..!!')


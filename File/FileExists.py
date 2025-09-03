import os
if os.path.isfile('student.txt'):
    f = open('student.txt')
    print('File Opened..!!')
    content = f.read()
    print(content)
    f.close()
else:
    print('File Not Found..!!')
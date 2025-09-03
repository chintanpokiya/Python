#creating connection

import mysql.connector
config = {
        'user':'root',
        'password':'',
        'host':'localhost',
        'database':'pdb',
        'port':3306
}
try:
    conn = mysql.connector.connect(**config)
    if(conn.is_connected()):
        print('connected successfully..!!')
except:
    print('Unable to Connect..!!')

sql='INSERT INTO student1(name,roll,fees) VALUES(%s,%s,%s)'
myc = conn.cursor()
sn = input("Enter Student Name :- ")
rn = input("Enter Student RollNo :- ")
sal = float(input("Enter Student salary :- "))
params = (sn,rn,sal)
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,'Row Inserted')
    print(f'Stu Id : {myc.lastrowid} Inserted')
except:
    print('Unable to Insert data')
myc.close()
conn.close()

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

sql='INSERT INTO student1(name,roll,fees) VALUES(%(n)s,%(r)s,%(f)s)'
myc = conn.cursor()
params = {'n':'Abhishek','r':777,'f':54100}
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,'Row Inserted')
    print(f'Stu Id : {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print('Unable to Insert data')
myc.close()
conn.close()

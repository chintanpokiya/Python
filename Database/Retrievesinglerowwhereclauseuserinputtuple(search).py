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

sql = 'SELECT * FROM student1 WHERE stuid=%s'
myc = conn.cursor()
n = int(input('Enter StuID to Display :- '))
disp_value = (n,)
try:
    myc.execute(sql, disp_value)
    row = myc.fetchone()
    print(row)
    print('Total rows :- ',myc.rowcount)
except:
    print('Unable to Retrieve data')
myc.close()
conn.close()

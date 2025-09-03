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

sql='SELECT * FROM student1 where name = "Neelkanth"'
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    print(row)
    print('Total rows :- ',myc.rowcount)
except:
    print('Unable to retrieve data')
myc.close()
conn.close()

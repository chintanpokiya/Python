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

sql='SELECT * FROM student1'
myc = conn.cursor()
try: 
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print('Total Rows :- ',myc.rowcount)
except:
    print('Unable to Retrieve Data')
myc.close()
conn.close()

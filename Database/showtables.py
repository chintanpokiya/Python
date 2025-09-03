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

sql='SHOW TABLES'
myc = conn.cursor()
myc.execute(sql)
for t in myc:
    print(t)
myc.close()
conn.close()

#creating connection

import mysql.connector
config = {
        'user':'root',
        'password':'',
        'host':'localhost',
        'port':3306
}
try:
    conn = mysql.connector.connect(**config)
    if(conn.is_connected()):
        print('connected successfully..!!')
except:
    print('Unable to Connect..!!')

sql='CREATE DATABASE pdb'
myc = conn.cursor()
myc.execute(sql)
myc.close()
conn.close()

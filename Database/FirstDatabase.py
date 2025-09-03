#creating connection

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port=3306
    )
    if(conn.is_connected()):
        print('connected successfully..!!')
except:
    print('Unable to Connect..!!')

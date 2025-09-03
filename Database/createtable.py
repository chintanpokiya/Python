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

sql='CREATE TABLE student1(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT, fees FLOAT)'
myc = conn.cursor()
myc.execute(sql)
myc.close()
conn.close()

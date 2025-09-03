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

sql='INSERT INTO student1(name,roll,fees) VALUES("Neelkanth", 28, 2500.24)'
myc = conn.cursor()
try: 
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'Row Inserted')
    print(f'Stu Id: {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print('Unable to Insert Data')
myc.close()
conn.close()

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

sql='UPDATE student1 SET fees=25000 where stuid=2'
myc = conn.cursor()
try: 
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'Row Updated')
except:
    conn.rollback()
    print('Unable to Update Data')
myc.close()
conn.close()

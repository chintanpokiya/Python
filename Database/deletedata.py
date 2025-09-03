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

sql='DELETE from student1 where stuid=4'
myc = conn.cursor()
try: 
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'Row Deleted')
except:
    conn.rollback()
    print('Unable to Delete Data')
myc.close()
conn.close()

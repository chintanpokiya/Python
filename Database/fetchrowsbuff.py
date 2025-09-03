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
myc = conn.cursor(buffered=True)
myc.execute(sql)
rows = myc.fetchmany(size=2)
for row in rows:
    print(row)
print('Total Rows :- ',myc.rowcount)
myc.close()
conn.close()

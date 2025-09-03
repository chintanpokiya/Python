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

sql='INSERT INTO student1(name,roll,fees) VALUES(%s,%s,%s)'
myc = conn.cursor()
seq_of_params = [
    ("Niti",222,3224.56),
    ("Mukesh",333,8675.45),
    ("Arjit",444,6574.76)]
try:
    myc.executemany(sql,seq_of_params)
    conn.commit()
    print(myc.rowcount,'Row Inserted')
    #print(f'Stu Id : {myc.lastrowid} Inserted')
except:
    conn.rollback()
    print('Unable to Insert data')
myc.close()
conn.close()

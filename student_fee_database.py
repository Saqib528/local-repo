import sqlite3

import os

if os.path.exists('student.db'):
    os.remove('student.db')

conn=sqlite3.connect('student.db')

cur=conn.cursor()
cur2=conn.cursor()
cur3=conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS student_data
            (

            std_id INTEGER PRIMARY KEY AUTOINCREMENT,
            std_name TEXT,
            std_class TEXT,
            std_email TEXT
            )

""")

cur2.execute("""
            CREATE TABLE IF NOT EXISTS student_fee
            (
            
            fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            std_id INTEGER,
            fee_amount INTERGER
            
            
            )""")

student_data=[

    ('Ali','12th','ali12@gmail.com'),
    ('Hamza','11th','hamza_awan@gmail.com'),
    ('Hamad','10th','hamad_ahmed@gmail.com'),
    ('Salman','10th','salman_ali@gmail.com')

]


student_fee=[

     (1,2000),
     (2,4000),
     (3,3000),
     (4,1200),
     (1,2000),
     (3,1400),
     (1,2500),
     (2,5000),
     (3,4000),
     (4,2500),
     (3,1200)

]

cur.executemany("INSERT INTO student_data (std_name,std_class,std_email)values(?,?,?)",student_data)


cur.execute("SELECT*FROM student_data")

rows=cur.fetchall()

for row in rows:
    print(row)
    print("")





cur2.executemany("INSERT INTO student_fee(std_id,fee_amount)VALUES(?,?)",student_fee)

cur2.execute("SELECT*FROM student_fee")

table=cur2.fetchall()
print("FEE_ID,STUDENT_ID,FEE_AMOUNT")
for i in table:
    print(i)
    print("")



conn.commit()
conn.close()


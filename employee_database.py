import sqlite3

conn= sqlite3.connect('employee.db')

cur = conn.cursor()

cur.execute("""
            
        CREATE TABLE IF NOT EXISTS employee_id (

        id INTEGER PRIMARY KEY AUTOINCREMENT,         
        name TEXT ,
        age INTEGER,
        e_mail TEXT,
        department TEXT
         
            )

""")

employee_id = [
   
       ('Ahmed ',24,'ahmed33@gmail.com','Assistant Manager'),
       ('Usama',27,'usama_mir@gmail.com','Accountant'),
       ('Danish',29,'danish_ali@gmail.com','HR')


    
]

cur.executemany('INSERT INTO employee_id(name,age,e_mail,department)VALUES(?,?,?,?)',employee_id)

conn.commit()

cur.execute(""" UPDATE employee_id SET department= 'Assistant Director'
            
            WHERE department = 'HR'

            """)

cur.execute("SELECT*FROM employee_id ")

row = cur.fetchall()

print("TABLE CONTENT")
for rows in row:
    print(rows)

conn.close()

import os

if os.path.exists('employee.db'):
    os.remove('employee.db')

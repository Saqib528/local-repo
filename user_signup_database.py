import sqlite3

import os 
if os.path.exists('sign_up.db'):
    os.remove('sign_up.db')

conn=sqlite3.connect('sign_up.db')

cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user(
            
           first_name TEXT,
           last_name TEXT,
            date_of_birth INTEGER,
            gender TEXT,
            e_mail TEXT
            
            
            )
""")

user=[
    ('Ali','Hassan',2001,'Male','hassanali22@gmail.com'),
    ('Umar','Ahmed',1995,'male','umar_ali19@gmail.com'),
    ('Muhammad','Waqar',2003,'Male','muhammad_waqar222@gmail.com'),
    ('Ayesha','Khan',2000,'Female','ayesha_khan@gmail.com'),
    ('Sadia','Hassan',2005,'Female','sadia_hassan121@gmail.com'),
    ('Maryam','Ahmed',2002,'Female','maryam1ahmed@gmail.com'),
    ('Salman','Nazir',1999,'Male','salman_nazir333@gmail.com')

]

cur.executemany("INSERT INTO user (first_name,last_name,date_of_birth,gender,e_mail)VALUES(?,?,?,?,?)",user)
cur.execute("ALTER TABLE user RENAME TO old_user")

cur.execute("""CREATE TABLE user(
            
            first_name TEXT,
            last_name TEXT,
            date_of_birth INTEGER,
            e_mail TEXT
            
            
            )


""")


cur.execute("""INSERT INTO user(first_name,last_name,date_of_birth,e_mail)
SELECT first_name,last_name,date_of_birth,e_mail FROM old_user
""")


cur.execute('DROP TABLE old_user')


conn.commit()

cur.execute("SELECT name FROM sqlite_master WHERE type ='table'; ")


tables=cur.fetchone()
if tables:
    print(f"THE EXISTING TABLE NAME IS : {tables[0]}")

    print("------------------------------------------------------------------")
    print("")
else:
    print("TABLE NOT FOUND ")

cur.execute("SELECT rowid, *FROM user")




row=cur.fetchall()

for rows in row:
    print(rows)

    print("")


cur.execute("SELECT *FROM user WHERE last_name = 'Ahmed' ")

row=cur.fetchall()
print("SELECTED ITEMS ARE :")
print("---------------------------------------------------------------")
for rows in row:
    print(rows)
    print("")


conn.close()


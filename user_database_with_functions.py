import sqlite3
import os 
if os.path.exists('user_database_for_app'):
    os.remove('user_database_for_app')

conn=sqlite3.connect('user_database_for_app')

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

conn.commit()
conn.close()

def database_tables():

    conn=sqlite3.connect('user_database_for_app')

    cur=conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    table=cur.fetchone()
     
    if table:
        print("")
        print(f".......................THE EXISTING TABLE........................")
        print("")
        print(f"                              {table[0]}                           ")

    else:
        print("THERE IS NO EXISTING TABLE IN DATABASE")
    


def show_all():

    conn=sqlite3.connect('user_database_for_app')
    cur=conn.cursor()

    cur.execute("SELECT rowid,*FROM user")

    row=cur.fetchall()
    print("")
    print("..........................USER_RECORD............................ ")
    print("------------------------------------------------------------------")
    for rows in row:

        print(rows)
        print("")


def add_record(first_name,last_name,date_of_birth,gender,e_mail):
    conn=sqlite3.connect('user_database_for_app')
    cur=conn.cursor()

    cur.execute("INSERT INTO user VALUES (?,?,?,?,?)",(first_name,last_name,date_of_birth,gender,e_mail))
    
    conn.commit()
    conn.close()

def delete_record(id):
    conn=sqlite3.connect('user_database_for_app')
    cur=conn.cursor()

    cur.execute("DELETE FROM user WHERE rowid=(?)",id)

    conn.commit()
    conn.close()




def add_many_record(list):
    conn=sqlite3.connect('user_database_for_app')
    cur=conn.cursor()

    cur.execute("INSERT INTO user VALUES (?,?,?,?,?)",(list))
    
    conn.commit()
    conn.close()

def where_clause(last_name):
    conn=sqlite3.connect('user_database_for_app')
    cur=conn.cursor()

    cur.execute("SELECT*FROM user WHERE last_name = (?)",(last_name,))
    row=cur.fetchall()
    
    print("")
    print("..........................USER_RECORD............................ ")
    print("------------------------------------------------------------------")
    for rows in row:

        print(rows)
        print("")


    

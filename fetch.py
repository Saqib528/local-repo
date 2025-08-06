import sqlite3

conn=sqlite3.connect('sign_up.db')

cur=conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type ='table'; ")


tables=cur.fetchone()
if tables:
    print(f"THE EXISTING TABLE NAME IS : {tables[0]}")
else:
    print("TABLE NOT FOUND ")

cur.execute("SELECT rowid, *FROM user ")

rows=cur.fetchall()
for row in rows:
    print(row)



#for table in tables :
    #print(table[0])

conn.close()
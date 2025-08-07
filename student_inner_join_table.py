import sqlite3

conn=sqlite3.connect('student.db')

cur3=conn.cursor()




cur3.execute("SELECT f.std_id,s.std_name,f.fee_amount FROM student_fee as f inner join student_data as s on f.std_id=s.std_id  ")  

new_table=cur3.fetchall()
for j in new_table:
    print(j)
    print("")

import sqlite3

conn=sqlite3.connect('student.db')

cur2=conn.cursor()

print("")
print("")
cur2.execute("SELECT COUNT(*) FROM student_fee")
count_of_entries=cur2.fetchone()[0]
print("Total entries in table ")
print(count_of_entries) 

print("")

cur2.execute("SELECT SUM(fee_amount) FROM student_fee")
total=cur2.fetchone()[0]
print("Sum of all amount ")
print(total)
print("")

cur2.execute("SELECT MAX(fee_amount) FROM student_fee")
max=cur2.fetchone()[0]
print("Max amount in fee ")
print(max)
print("")


cur2.execute("SELECT MIN(fee_amount) FROM student_fee")
min=cur2.fetchone()[0]
print("Min amount in fee ")
print(min)
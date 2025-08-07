import sqlite3

conn=sqlite3.connect('stud.db')

cur=conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS stud_data
            (

            std_id INTEGER PRIMARY KEY AUTOINCREMENT,
            std_name TEXT,
            std_class TEXT,
            std_email TEXT
            )

""")

stud_data=[

    ('Ali','12th','ali12@gmail.com'),
    ('Hamza','11th','hamza_awan@gmail.com'),
    ('Hamad','10th','hamad_ahmed@gmail.com'),
    ('Salman','10th','salman_ali@gmail.com')

]

cur.executemany("INSERT INTO stud_data (std_name,std_class,std_email)values(?,?,?)",stud_data)
cur.execute("ALTER TABLE stud_data ADD COLUMN result TEXT  ")
#cur.execute("UPDATE stud_data SET result='Pass' WHERE std_name='Ali' AND UPDATE  SET result='Fail WHERE std_name ='Hamza'")
cur.execute("""
      
      UPDATE stud_data
      SET result= CASE
    WHEN std_name='Ali' THEN 'Pass'
    WHEN std_name='Hamza' THEN 'Fail'
    ELSE result 
    END
    WHERE std_name IN ('Ali','Hamza')

""")


cur.execute("SELECT*FROM stud_data")

rows=cur.fetchall()

for row in rows:
    print(row)
    print("")



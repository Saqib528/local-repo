import sqlite3

conn=sqlite3.connect('cars.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cars_data(
            
            company TEXT,
            car_name TEXT,
            model INTEGER,
            colour TEXT,
            category TEXT

            
          )

         """)

cars_data=[
    
        ('BMW','M4',2022,'Blue','sports'),
        ('TOYOTA','SUPRA',2015,'char_coal grey ','sports'),
        ('FORD','MUSTANG',2025,'jet_black','sports'),
        ('HONDA','CIVIC',2022,'black','sports'),
        ('DOGDE','CHALLENGER',2013,'yellow','sports')

]

cur.executemany("INSERT INTO cars_data(company,car_name,model,colour,category)VALUES(?,?,?,?,?)",cars_data)


conn.commit()

cur.execute("SELECT *FROM  cars_data")

row=cur.fetchall()

print(" TABLE OF CONTENT")
for rows in row:
    print(rows)

conn.close()
import os 
if os.path.exists('cars.db'):
    os.remove('cars.db')
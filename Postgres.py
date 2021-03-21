# Connect into DB on the PC Саша

import psycopg2

con = psycopg2.connect(
  database="vvvnik",
  user="postgreadmin",
  password="123",
  host="localhost",
  port="5432"
)
print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')

cur.execute(
  "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'John', 18, 'Computer Science', 'ICT')"
)

print("Record inserted successfully")

con.commit()
con.close()

import sqlite3

print("Hello World")
conn = sqlite3.connect('mydb.db')
curr = conn.cursor()
print(curr)
#curr.execute('INSERT INTO emp(empid,empname,email) VALUES (2,"Elle","test1@test.com")')
curr.execute('SELECT * FROM emp')
conn.commit()
rows = curr.fetchall()
print(rows)
conn.close()
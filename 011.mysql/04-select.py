
import mysql.connector as con

database = con.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin",
    database="productos"
)

cursor = database.cursor()

sql = "SELECT * FROM product;"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()
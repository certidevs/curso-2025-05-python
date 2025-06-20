
import mysql.connector as con

database = con.connect(
    host="127.0.0.1", 
    port="3306", 
    user="root", 
    password="admin", 
    database="productos"
)
cursor = database.cursor()

sql = """
UPDATE product
SET name = %s, price = %s, quantity = %s
WHERE id = %s;
"""
params = ("mesa de roble añejo", 811.9, 2, 1)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

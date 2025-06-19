
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
 DELETE FROM product 
 WHERE id = %s; 
"""
params = (1,) # tupla
cursor.execute(sql, params) # una vez borrado, la secuencia de ids, continúa, no se resetea

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

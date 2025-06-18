"""
Crear nueva base de datos
"""
import mysql.connector as con

database = con.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin"
)
cursor = database.cursor()
sql = """
DROP DATABASE IF EXISTS productos;
"""
cursor.execute(sql)

sql = """
CREATE SCHEMA `productos` 
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci ;
"""
cursor.execute(sql)

cursor.close()
database.close()

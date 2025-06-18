"""
Crear nueva tabla en la base de datos
"""
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
CREATE TABLE IF NOT EXISTS product(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(8, 2),
    quantity INT
);
"""
cursor.execute(sql)

cursor.close()
database.close()

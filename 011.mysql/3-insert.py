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
INSERT INTO product (name, price, quantity)
VALUES (%s, %s, %s);
"""
params = ('mesa de roble', 499.99, 2)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()


# 1 - importar driver
import mysql.connector as con

# Crear conexión a base de datos
database = con.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin"
)

# Obtener el objeto cursor:
cursor = database.cursor()

# Ejecutar codigo SQL:
sql = """
SHOW DATABASES;
"""
cursor.execute(sql)

# Procesar resultados
for name in cursor:
    print(name)

# Cerrar recursos:
cursor.close()
database.close()

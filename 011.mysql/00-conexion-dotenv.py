# pip install mysql-connector-python
# 1 - importar driver
import mysql.connector as con
from dotenv import load_dotenv
import os

# tiene que existir un archivo .env con la contraseña AZURE_MYSQL_PASS=securepassword
# ese archivo .env se ignora en git y no se sube a un repositorio
load_dotenv()

# Crear conexión a base de datos
database = con.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password=os.getenv("AZURE_MYSQL_PASS")
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

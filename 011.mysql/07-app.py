import mysql.connector
from mysql.connector import Error

generic_mysql_conn = {
    'user': 'root',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '3306'
}
ecommerce_mysql_conn = {
    'user': 'root',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'ecommerce',
}

class Product:
    def __init__(self, id, name, sku, quantity, price):
        self.id = id
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'Product(id:{self.id}, name:{self.name}, sku:{self.sku}, quantity:{self.quantity}, price:{self.price})'

    def __repr__(self):
        return self.__str__()


def create_ecommerce_db():
    """
    Función que crea una nueva base de datos ecommerce en MySQL.
    En caso de que ya exista la borra y la crea de nuevo.
    Dentro de la base de datos 'ecommerce' crea la tabla products
    """
    try:
        db = mysql.connector.connect(**generic_mysql_conn)
        cursor = db.cursor()

        # Borramos la base de datos en caso de que ya exista
        cursor.execute("DROP database IF EXISTS ecommerce")

        # sintaxis sql para crear base de datos
        cursor.execute("CREATE SCHEMA `ecommerce` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci;")

        # sintaxis sql para crear una tabla
        sql = '''CREATE TABLE ecommerce.products(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            sku VARCHAR(20),
            quantity INT,
            price FLOAT
        )'''
        cursor.execute(sql)
        cursor.close()
        db.close()
    except Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


# ********************* FUNCIONES PARA LECTURA DE PRODUCTOS POR CONSOLA ******************************************

def read_new_product_input():
    """
    Lee los datos de un nuevo producto introducido por el usuario a través de la consola.
    El producto no tiene id ya que todavía no existe en base de datos.
    Returns
    -------
    product
        un objeto de la clase Product con los datos leídos de la consola
    """
    name, sku, quantity, price = '', '', 0, 0.0
    read = True
    while read:
        try:
            name = name if name else str(input("Introduce el nombre de producto: "))
            sku = sku if sku else str(input("Introduce el sku de producto: "))
            quantity = quantity if quantity else int(input("Introduce la cantidad de producto: "))
            price = price if price else float(input("Introduce el precio del producto: "))
            read = False
        except ValueError as error:
            print(error)
    return Product(None, name, sku, quantity, price)


def read_product_input():
    """
    Lee los datos de un producto existente introducidos por el usuario a través de la consola.
    Necesario que el producto tenga un id.
    Returns
    -------
    product
        un objeto de la clase Product con los datos leídos de la consola
    """
    product_id, name, sku, quantity, price = 0, '', '', 0, 0.0
    read = True
    while read:
        try:
            product_id = product_id if product_id else int(input("Introduce el id de producto a modificar: "))
            name = name if name else str(input("Introduce el nuevo nombre de producto: "))
            sku = sku if sku else str(input("Introduce el nuevo sku de producto: "))
            quantity = quantity if quantity else int(input("Introduce la nueva cantidad de producto: "))
            price = price if price else float(input("Introduce el nuevo precio del producto: "))
            read = False
        except ValueError as error:
            print(error)
    return Product(product_id, name, sku, quantity, price)


# ********************* FUNCIONES CRUD ***************************************************************

def create_product(product):
    """
    Crea un producto en base de datos

    Parámetros
        ----------
        product : Product
            Objeto producto con los datos de producto para almacenar en base de datos
    """
    try:
        db = mysql.connector.connect(**ecommerce_mysql_conn)
        cursor = db.cursor()

        sql = '''INSERT INTO products 
        (name, sku, quantity, price) 
        VALUES (%s, %s, %s, %s)'''
        params = (product.name, product.sku, product.quantity, product.price)

        cursor.execute(sql, params)
        db.commit()

        print(cursor.rowcount, "producto/s insertado/s en base de datos.")
    except Error as error:
        print("Error inserting one product from database", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


def update_product(product):
    """
    Actualiza un producto existente en base de datos

    Parámetros
        ----------
        product : Product
            Objeto producto con los datos de producto para almacenar en base de datos
    """
    try:
        db = mysql.connector.connect(**ecommerce_mysql_conn)
        cursor = db.cursor()
        sql = '''
        UPDATE products 
        SET name = %s, sku = %s, quantity = %s, price = %s 
        WHERE id = %s'''

        params = (product.name, product.sku, product.quantity, product.price, product.id)

        cursor.execute(sql, params)
        db.commit()
        print(cursor.rowcount, "producto/s modificado/s en base de datos.")
    except Error as error:
        print("Error updating product from database", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


def find_product_by_id(id):
    """
    Recupera un producto de base de datos a partir de su id

    Parámetros
        ----------
        id : int
            El identificador del producto a recuperar de base de datos
    Returns
    -------
    list
        una lista de productos
    """
    try:
        db = mysql.connector.connect(**ecommerce_mysql_conn)
        cursor = db.cursor()
        sql = 'SELECT * FROM products WHERE id = %s'
        params = (id,)  # Asegurarse de que sea una tupla

        cursor.execute(sql, params)  # Pasar la tupla con los valores

        result = cursor.fetchone()
        product = Product(result[0], result[1], result[2], result[3], result[4])
        return product
    except Error as error:
        print("Error finding one product from database", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


def find_all_products():
    """
    Recupera todos los productos de base de datos

    Returns
    -------
    list
        una lista de productos
    """
    try:
        db = mysql.connector.connect(**ecommerce_mysql_conn)
        cursor = db.cursor()
        sql = 'SELECT * FROM products'
        cursor.execute(sql)
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append(Product(row[0], row[1], row[2], row[3], row[4]))
        return products
    except Error as error:
        print("Error finding all products from database", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


def delete_product(id):
    """
    Borra un producto de la base de datos a partir de su campo id

    Parámetros
        ----------
        id : int
            El identificador del producto a eliminar de base de datos
    """
    try:
        db = mysql.connector.connect(**ecommerce_mysql_conn)
        cursor = db.cursor()
        sql = "DELETE FROM products WHERE id = %s"
        params = (id,)
        cursor.execute(sql, params)
        db.commit()
        print(cursor.rowcount, "producto/s borrado/s en base de datos.")
    except Error as error:
        print("Error deleting product from database", error)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()


# ********************* CÓDIGO PARA EL PROGRAMA ***************************************************************

create_ecommerce_db()

action = ''
while action != "Salir":
    try:
        action = int(input(
            "Introduce una acción a realizar:\n"
            "1 - Consultar producto \n"
            "2 - Consultar todos los productos\n"
            "3 - Crear producto \n"
            "4 - Modificar producto\n"
            "5 - Borrar producto \n"
            "6 - Salir\n"))

        if action == 1:  # Consultar producto
            prodId = str(input("Introduce el id del producto a consultar: "))
            product = find_product_by_id(prodId)
            print('Producto encontrado: ', product)

        elif action == 2:  # Consultar todos los productos
            products = find_all_products()
            print('Productos en base de datos: ', products)

        elif action == 3:  # Crear producto
            product = read_new_product_input()
            create_product(product)

        elif action == 4:  # Modificar producto
            product = read_product_input()
            update_product(product)

        elif action == 5:  # Borrar producto
            prodId = str(input("Introduce el id del producto a borrar: "))
            delete_product(prodId)

        elif action == 6:  # Terminar el programa
            print("Goodbye!")
            break

    except Exception as e:
        print(e)

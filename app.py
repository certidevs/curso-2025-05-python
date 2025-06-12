# Opción 1: importar todo
# import app_funciones

# Opción 2: importar todo con alias, normalmente para usar un nombre más corto
# import app_funciones as defs

# Opción 3: importar solo lo necesario
# from app_funciones import mostrar_productos

menu = """
Aplicación CRUD de productos:
1 - READ - Ver productos
2 - CREATE - Crear nuevo producto
3 - UPDATE - Actualizar producto
4 - DELETE - Borrar producto
5 - Salir 
"""

# Lista de strings, la vamos usar como si fuera una base de datos
# esto se puede reemplazar por una lista de objetos de la clase Producto

class Product:
    def __init__(self, name: str, price: float, quantity: int, published: bool):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.published = published

# crear objetos Product
products = [
    Product('Producto 1', 19.99, 5, True),
    Product('Producto 2', 29.99, 10, True)
]

def mostrar_productos(products):
    # Opción 1: imprimir todos los productos de golpe:
    # print(products)

    # Opción 2: imprimir los productos pero de uno en uno
    # for product in products:
    #     print(product)

    # Opción 3: imprimir con el índice:
    if len(products) == 0:
        print('No hay productos')
        return
    
    for i, product in enumerate(products):
        print(f'Producto {i}: {product}')


def crear_producto():

    product_name = input("Introduce el nombre del nuevo producto")
    if not product_name:
        print("Nombre incorrecto")
        return

    product_price = float(input("Introduce el precio en euros del producto sin prefijo. Ejemplo: 15.99"))
    if product_price < 0:
        print ("Precio no puede ser negativo")
        return
    
    product_quantity = int(input("Introduce unidades de producto (stock). Ejemplo: 5"))
    if product_quantity < 0:
        print ("Cantidad no puede ser negativo")
        return
    
    product_published_input = input('¿El producto está publicado? (y/n):').lower().strip()
    # product_published = product_published_input == 'y' or product_published_input == 'yes' or product_published_input == 'si'
    product_published = product_published_input == 'y'

    # ya tenemos todos los valores para crear un nuevo Producto
    new_product = Product(product_name, product_price, product_quantity, product_published)
    products.append(new_product)
    print('Producto creado correctamente')


def editar_producto():
    mostrar_productos(products)

    id_product = int(input('Introduce el id del producto que quieres modificar'))

    # TODO verificar que el id sea correcto:
    # no puede ser menor que 0
    # no puede ser mayor de 20
    if 0 <= id_product < len(products):
        products[id_product] = input("Introduce el nuevo nombre para el producto") 
    else:
        print("id introducido no es correcto")

def mostrar_menu_y_leer_opcion():
    print(menu)
    print('\n')

    try:
        return int(input("Introduce una opción:\n"))
    except ValueError:
        print("Error, la opción debe ser un número de 1 a 5.")

    return 0

while True:
    option = mostrar_menu_y_leer_opcion()
    if option == 1:
        mostrar_productos(products)
    elif option == 2:
        crear_producto()
    elif option == 3:
        editar_producto()
    elif option == 4:
        editar_producto()
    elif option == 5:
        print("Saliendo del programa")
        break
    else:
        print('no has seleccionado una opción correcta')

# El programa termina tras la primera interacción

# En una aplicación de consola si queremos el programa continúe en marcha 
# necesitamos estructuras iterativas

# En una aplicación web (flask, fastapi, django) es el framework quien controla la ejecución
# del programa y lo mantiene en marcha

## TODO agregar campo id para simular una clave primaria como en base de datos
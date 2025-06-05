
menu = """
Aplicación CRUD de productos:
1 - READ - Ver productos
2 - CREATE - Crear nuevo producto
3 - UPDATE - Actualizar producto
4 - DELETE - Borrar producto
5 - Salir 
"""

# Lista de strings, la vamos usar como si fuera una base de datos
products = ["ordenador MSI modern 15", "ordenador HP pavilion"]

def mostrar_productos():
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
    try:
        new_product = input("Introduce el nombre del nuevo producto")

        # # Opción 1
        # # validar que el producto esté correcto
        if new_product.strip(): #verificar que no esté vacío
            products.append(new_product)
            print("producto guardado correctamente")
        else:
            print("Error, el producto no puede estar vacío")

        # opción 2
        # if len(new_product) == 0: #cuidado, si el producto solo tiene espacios lo da por bueno sí tendrá longitud
        #     print("Error, el producto no puede estar vacío")
        #     return
        
        # products.append(new_product)

    except ValueError:
        print("error al guardar nuevo producto")

def editar_producto():
    mostrar_productos()

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
    option = int(input("Introduce una opción:\n"))
    return option

while True:
    option = mostrar_menu_y_leer_opcion()
    if option == 1:
        mostrar_productos()
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
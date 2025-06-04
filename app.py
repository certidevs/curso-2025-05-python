
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

while True:
    print(menu)
    print('\n')
    option = int(input("Introduce una opción:\n"))

    if option == 1:
        # Opción 1: imprimir todos los productos de golpe:
        # print(products)

        # Opción 2: imprimir los productos pero de uno en uno
        # for product in products:
        #     print(product)

        # Opción 3: imprimir con el índice:
        for i, product in enumerate(products):
            print(f'Producto {i}: {product}')

    elif option == 2:
        
        try:
            new_product = input("Introduce el nombre del nuevo producto")
            products.append(new_product)
        except ValueError:
            print("error al guardar nuevo producto")

    elif option == 3:
        
        for i, product in enumerate(products):
            print(f'Producto {i}: {product}')

        id_product = int(input('Introduce el id del producto que quieres modificar'))

        # verificar que el id sea correcto:
        # no puede ser menor que 0
        # no puede ser mayor de 20
        if 0 <= id_product < len(products):
            products[id_product] = input("Introduce el nuevo nombre para el producto") 
        else:
            print("id introducido no es correcto")

    elif option == 4:
        
        id_product = int(input('Introduce el id del producto que quieres borrar'))
        # products.remove(products[id_product])
        try:
            deleted_product = products.pop(id_product)
            print(f"Producto borrado con éxito: {deleted_product}")
        except IndexError:
            print("El producto no se ha encontrado: 404 not found")

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
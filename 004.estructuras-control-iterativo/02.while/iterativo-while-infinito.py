class Product:
    pass

def consultar_productos():
    pass


def crear_producto(producto):
    pass


while True:
    print(
        """
Bienvenido/a! Elige una opción:
1 - Consultar productos
2 - Crear nuevo producto
3 - Borrar producto
4 - Salir
        """
    )

    number = int(input("Introduce una opción: "))

    if number == 1:
        print("Option 1")
        consultar_productos()

    elif number == 2:
        print("Option 2")
        product = Product()
        crear_producto(product)

    elif number == 3:
        id_product = int(input("Introduce el id del producto a borrar: "))
        print("Borrando el producto ...", id_product)
        print("El producto ha sido borrado.")

    elif number == 4:
        print("Fin del programa")
        break

    else:
        print("Introduce una opción válida")

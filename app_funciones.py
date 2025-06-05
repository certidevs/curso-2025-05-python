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


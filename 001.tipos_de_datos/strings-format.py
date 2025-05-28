cost = 49
description = "El precio del producto es {} euros"
print(description.format(cost))

quantity = 5
itemID = 567
price = 49
# Al utilizar llaves le indicamos que las rellene con las variables que pasamos en format
orderDescription = "Compra de {} piezas del producto con id {} con precio {:.2f} euros."
print(orderDescription.format(quantity, itemID, price))

# Al especificar una posición dentro de las llaves le estamos dando un orden
orderDescription = "Compra de {0} piezas del producto con id {1} con precio {2:.2f} euros."
print(orderDescription.format(quantity, itemID, price))

# Podemos repetir variables o cambiarlas de orden
orderDescription = "Compra de {0} piezas del producto con id {1} con precio {2:.2f} euros. Cantidad total = {0}"
print(orderDescription.format(quantity, itemID, price))

# En vez de usar números podemos usar nombres
orderDescription = "Compra de {quantity} piezas del producto con id {itemID} con precio {price:.2f} euros."
print(orderDescription.format(quantity=quantity, itemID=itemID, price=59.9))

# Para formatear podemos usar :< dentro de las llaves para indicar que queremos
# forzar a alinear a la izquierda un texto con los espacios indicados
head = "Producto\tCantidad"
description = "{0:<15}\t{1}"
print(head)
print(description.format("Coche", 2))
description = "{0}\t{1}"
# Observar la diferencia sin el formateo de espacios
print(description.format("Coche", 2))


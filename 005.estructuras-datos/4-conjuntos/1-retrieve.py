
laptops = {"asus", "dell", "hp", "msi", "lenovo"}

print(laptops)  # Fijarse que cambia en cada ejecución

# No está indexado, no es posible acceder por índice: TypeError: 'set' object is not subscriptable
# print(laptops[0])

# Accedemos por medio de estructuras de control iterativo
for laptop in laptops:
    print(laptop)



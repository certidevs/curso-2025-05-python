
# No se puede modificar un elemento
# Nota: se podría borrar el elemento y añadir uno nuevo
laptops = {"asus", "dell", "hp", "msi", "lenovo", "ibm"}

# laptops[0] = "ibm"  # TypeError: 'set' object does not support item assignment

# Comprobar si tiene un elemento

print("asus" in laptops)  # True
print("sdfsdf" in laptops)  # False


# Comprobar su longitud

print("La longitud del set es", len(laptops))



def print_laptops():
    print(laptops)
    print("Longitud del conjunto de ordenadores:", len(laptops))
    print("********************")


laptops = {"asus", "dell", "hp", "msi", "lenovo", "ibm"}

print_laptops()

# 1. remove() - lanza excepción si existe
laptops.remove("asus")

print_laptops()

# laptops.remove("asus")  # KeyError: 'asus' - Falla porque ya no existe
print_laptops()

# 2. discard() - no lanza excepción si no existe
laptops.discard("lenovo")
print_laptops()

laptops.discard("lenovo")
print_laptops()

# 3. pop() - borra un elemento cualquiera

laptop = laptops.pop()
print_laptops()
print(laptop)

# laptops.pop()
# laptops.pop()
# laptops.pop()
# laptops.pop()  # KeyError: 'pop from an empty set'
print_laptops()

# 4. Borrar con del

# del laptops[0] # TypeError: 'set' object doesn't support item deletion

# del laptops
# print_laptops()  #NameError: name 'laptops' is not defined -- Ha sido borrado ya no se puede imprimir


# 5. Vaciar un conjunto:

laptops.clear()
print_laptops()

laptops.clear()
print_laptops()

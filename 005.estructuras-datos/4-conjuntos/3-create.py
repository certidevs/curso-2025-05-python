
laptops = {"asus", "dell", "hp", "msi", "lenovo", "ibm"}


def print_laptops():
    print(laptops)
    print("Longitud del conjunto de ordenadores:", len(laptops))
    print("********************")


# Agregar un elemento al conjunto
laptops.add("apple")
laptops.add("acer")

print_laptops()

laptops.add("acer")

print_laptops()

# Agregar más de un elemento

# laptops.add("corsair", "MSFT")  # TypeError: add() takes exactly one argument (2 given)

laptops.update(["corsair", "MSFT"])  # Lista
print_laptops()

laptops.update({"test1": "prueba", "test2": "ejemplo"})  # Diccionario
print_laptops()

laptops.update({"test3", "test4"})  # Conjunto
print_laptops()

laptops.update(("test5", "test6"))  # Tupla
print_laptops()


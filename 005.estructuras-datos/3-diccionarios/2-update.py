customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}
print(customer)
customer["first_name"] = "Prueba"

# Esto no modifica, si no que inserta nuevos elementos
customer[0] = "Prueba"
customer[1] = "Ejemplo 2"
print(customer)

# Ejemplo leer de terminal
manufacturer = input("Introduce el fabricante: ")
print("El fabricante es", manufacturer)

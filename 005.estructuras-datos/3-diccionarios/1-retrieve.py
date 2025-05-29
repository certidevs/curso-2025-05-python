customer1 = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99
}

aprobado = True

# Para acceder a los valores utilizamos las claves
print(customer1)
print(customer1[0])
print(customer1["customer_id"])
print(customer1["married"])
print(type(customer1.get("married")))
# print(customer1["notexist"])  # No existe y dará fallo

# Especificar valor por defecto en caso de que no se encuentre la clave
print(customer1.get("english", 1))

# Verificar si un elemento existe

print("first_name" in customer1)

# Verificar longitud
print(len(customer1))
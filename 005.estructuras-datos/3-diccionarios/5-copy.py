
customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}

# IMPORTANTE ⛔: esto no copia !
customer2 = customer

customer["first_name"] = "ISABEL"

print(customer)
print(customer2)

# Método copy
customer3 = customer.copy()
customer["last_name"] = "Apellido"

print(customer)
print(customer3)

# Utilizar el constructor:


customer_base = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}
customer2 = dict(customer_base)
print(customer2)

customer4 = dict(customer_id=1, first_name="Alan", last_name="Sastre")
print(customer4)


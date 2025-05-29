customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}

# KEYS
keys = customer.keys()
print(keys)
print(type(keys))
customer["prueba"] = "test"
print(keys)  # Este objeto vista también recibe los cambios realizados sobre el diccionario

# VALUES
values = customer.values()
print(values)
print(type(values))

# ITEMS:
items = customer.items()
print(items)
print(type(items))

laptop = {
    "id": 1,
    "manufacturer": "Asus",
    "model": "K55A",
    "ram": 8,
    "color": "black",
    "img": "laptop-1.png"
}

customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}

# pop()
customer.pop("last_name")
# customer.pop() # Da error porque espera un argumento
# customer.pop("skdjfksfdj")  # KeyError
print(customer)


# popitem()
customer.popitem()
customer.popitem()
customer.popitem()
customer.popitem()
customer.popitem()
# customer.popitem() # KeyError: 'popitem(): dictionary is empty'
print(customer)

# palabra reservada del
del customer

customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}

# Vaciar el diccionario
customer.clear()
print(customer)

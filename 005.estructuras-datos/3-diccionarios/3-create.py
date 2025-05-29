customer = {
    "customer_id": 1,
    "store_id": 1,
    "first_name": "MARY",
    "last_name": "SMITH",
    "married": True,
    "salary": 99999.99,
}
print(customer)

customer["married"] = False  # Modifica
customer["email"] = "MARY.SMITH@sakilacustomer.org"  # Inserta

print(customer)

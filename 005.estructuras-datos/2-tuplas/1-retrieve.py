
nominados = ("Alan", "Alba", "Zacarias", "Aroa", "Dani", "Evaristo", "Mario", "Leticia", "Alan", "Alan")

print(nominados)
print(type(nominados))
print(nominados[0])
print(nominados[1])

for nominado in nominados:
    print(nominado)

"""
Listas: almacenan datos homogéneos por ejemplo:
    - objetos de la clase Car
    - nombres
    
Tuplas: almacenan datos heterogéneos por ejemplo:
    - columnas de la tabla car
"""
customer1 = (1, "Alan", "Sastre", "alan@alansastre.co", 1, 5)
customer2 = (2, "PATRICIA", "WILLIAMS", "PATRICIA.JOHNSON@sakilacustomer.org", 1, 5)
customer3 = (3, "BARBARA", "BROWN", "ELIZABETH.BROWN@sakilacustomer.org", 1, 5)
customers = [customer1, customer2, customer3]

# SELECT * FROM customer
# INSERT INTO customer
# UPDATE SET
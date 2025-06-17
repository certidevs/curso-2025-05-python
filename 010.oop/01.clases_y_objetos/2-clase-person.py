
# 1 - Crear una clase
class Person:

    # 1.1 Atributos de clase
    first_name = "Juan"
    last_name = "García"
    age = 33
    email = "juan@company.com"
    married = True
    salary = 40999.99


# 2 - Crear objetos (instancias) de la clase Person
juan = Person()
roberto = Person()
alberto = Person()

# 3 - Acceder a los atributos de clase a partir de un objeto

print(juan.first_name)
print(juan.married)
print("=====================")
print(roberto.first_name)
print("=====================")
print(alberto.first_name)

# 4 - Cambiar datos de un objeto

roberto.first_name = "Roberto"
roberto.email = "roberto@company.com"

alberto.first_name = "Alberto"

print("fin")

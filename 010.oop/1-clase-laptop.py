import datetime


# 1 - Crear una clase
class Laptop:
    manufacturer = ""
    model = ""
    price = 0
    overclock = False
    creation_date = datetime.datetime.now()
    market_release = datetime.date.today()


# 2 - Utilizar una clase
laptop1 = Laptop()
laptop2 = Laptop()
laptop3 = Laptop()
laptop4 = Laptop()

print(laptop1.manufacturer)
print(laptop1.model)
print("======================")
laptop1.manufacturer = "Acer"
print(laptop1.manufacturer)
print(laptop2.manufacturer)

class Vehicle:

    def __init__(self, id, manufacturer, model, price):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Car(Vehicle):

    def __init__(self, num_passengers, num_doors):
        self.num_passengers = num_passengers
        self.num_doors = num_doors


car = Car(5, 5)
# El problema de este enfoque es que tenemos que añadir el valor de los otros atributos fuera del constructor
car.id = 1
car.manufacturer = "Honda"
car.model = "CXZ3"
car.price = 50000.0

print(car.manufacturer)
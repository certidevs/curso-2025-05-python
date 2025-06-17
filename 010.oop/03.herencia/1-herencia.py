class Vehicle:

    num_ruedas = 2

    def __init__(self, id, manufacturer, model, price):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def acelerar(self):
        print("Acelerando de 0 a 120")


class Car(Vehicle):
    pass


class MotorCycle(Vehicle):
    pass


car = Car(1, "Fiat", "Bravo", 23000.0)
motorcycle = MotorCycle(1, "Kawasaki", "Ninja", 20000.0)

car.acelerar()
motorcycle.acelerar()
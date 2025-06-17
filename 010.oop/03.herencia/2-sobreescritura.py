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


class Tractor(Vehicle):
    def acelerar(self):  # Tractor sobreescribe el método acelerar()
        print("Cambiando de modo tortuga a modo liebre!")


car = Car(1, "Fiat", "Bravo", 23000.0)
motorcycle = MotorCycle(1, "Kawasaki", "Ninja", 20000.0)
tractor = Tractor(1, "John", "Deere", 45000)

car.acelerar()
motorcycle.acelerar()
tractor.acelerar()  # Sobreescrito: imprime el de la clase Tractor

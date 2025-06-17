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
    def __init__(self, num_passengers, num_doors):
        self.num_passengers = num_passengers
        self.num_doors = num_doors


class MotorCycle(Vehicle):
    def __init__(self, naked=False, passenger=True):
        self.naked = naked
        self.passenger = passenger


class Tractor(Vehicle):
    def acelerar(self):  # Tractor sobreescribe el método acelerar()
        print("Cambiando de modo tortuga a modo liebre!")


car = Car(5, 5)
car.id = 1
car.manufacturer = "Volkswagen"
car.model = "Golf"
car.price = 45000

motorcycle = MotorCycle(True, True)
motorcycle.id = 1
motorcycle.manufacturer = "KTM"
motorcycle.model = "Duke"
motorcycle.price = 5000
print("fin")


# motorcycle = MotorCycle(1, "Kawasaki", "Ninja", 20000.0)
# tractor = Tractor(1, "John", "Deere", 45000)
#
# car.acelerar()
# motorcycle.acelerar()
# tractor.acelerar()  # Sobreescrito: imprime el de la clase Tractor

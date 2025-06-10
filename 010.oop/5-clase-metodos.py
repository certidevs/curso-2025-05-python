class Car:
    # Atributos de clase
    num_ruedas = 4
    encendido = False
    velocidad = 0

    # Método constructor
    def __init__(self, manufacturer="", model="", color="", cc=0.0, cv=0.0, peso=0.0):
        # Atributos de instancia
        # tipos básicos
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cc = cc
        self.cv = cv
        self.peso = peso
        # asociaciones o relationships

    # Métodos (Comportamiento)
    def encender(self):
        self.encendido = True

    def apagar(self):
        # self.velocidad = 0  # Opción 1: reducir automáticamente la velocidad
        # Opción 2: obligar al usuario a reducir primero la velocidad a 0
        if self.velocidad == 0:
            self.encendido = False
            print("Coche apagado satisfactoriamente")
        else:
            print("Obligatorio reducir la velocidad a 0 para poder apagar el coche")

    def cambiar_velocidad(self, velocidad):
        if self.encendido and velocidad in range(0, 121):
            self.velocidad = velocidad
            print("Velocidad modificada correctamente")
        else:
            print("Obligatorio encender o que la velocidad sea correcta")

    def get_velocidad(self):
        return self.velocidad


# Uso de métodos:

ford_mondeo = Car("Ford", "Mondeo", "black", 1.4, 120, 1459.38)

print(ford_mondeo.encendido)
# comprobar encendido
ford_mondeo.encender()
print(ford_mondeo.encendido)

# apagar
ford_mondeo.apagar()
print(ford_mondeo.encendido)

# acelerar con el coche apagado - no acelera
ford_mondeo.cambiar_velocidad(50)
print(ford_mondeo.velocidad)

# encender
ford_mondeo.encender()
# acelerar con el coche encendido - si acelera porque la velocidad está entre 0 y 120
ford_mondeo.cambiar_velocidad(50)
print(ford_mondeo.velocidad)

# acelerar con el coche encendido - no acelera porque la velocidad no está entre 0 y 120
ford_mondeo.cambiar_velocidad(150)
print(ford_mondeo.velocidad)  # 50

# acelerar con el coche encendido
ford_mondeo.cambiar_velocidad(120)
print(ford_mondeo.velocidad)  # 120

# acelerar con el coche encendido
# ford_mondeo.acelerar(0)
# print(ford_mondeo.velocidad)  # 0

# apagar con el coche en velocidad - no apaga, obliga a reducir primero a 0
print("=================")
ford_mondeo.apagar()
print(ford_mondeo.velocidad)
print(ford_mondeo.encendido)

ford_mondeo.cambiar_velocidad(0)
ford_mondeo.apagar()

print(ford_mondeo.get_velocidad())

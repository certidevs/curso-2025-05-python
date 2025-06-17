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

    # Métodos especiales

    def __str__(self):
        """
        Método especial para obtener una representación textual del objeto
        :return:
        """
        return f"Car(num_ruedas={self.num_ruedas}, " \
               f"encendido= {self.encendido}, " \
               f"velocidad= {self.velocidad}, " \
               f"manufacturer= {self.manufacturer}, " \
               f"model= {self.model}, " \
               f"color= {self.color}, " \
               f"cc= {self.cc}, " \
               f"cv= {self.cv}, " \
               f"peso= {self.peso}" \
               f")"

    def __repr__(self):
        return self.__str__()


ford_mondeo = Car("Ford", "Mondeo", "black", 1.4, 120, 1459.38)
fiat_multipla = Car("Fiat", "Múltipla", "light grey", 1.2, 55, 900)

# Borrar propiedades
 # del ford_mondeo.manufacturer
ford_mondeo.manufacturer = "The new Ford"  # Volver a asociar un atributo eliminado
print(ford_mondeo)

# Borrar un objeto
del ford_mondeo
print(ford_mondeo)

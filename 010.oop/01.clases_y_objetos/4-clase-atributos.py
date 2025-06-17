# 1 - crear clase
class Car:
    # 1.1. Atributos de clase
    num_ruedas = 4
    encendido = False

    # 1.2 Método constructor
    def __init__(self, manufacturer="", model="", color="", cc=0.0, cv=0.0, peso=0.0):
        # Atributos de instancia
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cc = cc
        self.cv = cv
        self.peso = peso


# 2- Crear objetos de la clase Car
ford_mondeo = Car("Ford", "Mondeo", "black", 1.4, 120, 1459.38)
tesla_model_s = Car("Tesla", "Model S", "red", 2.1, 180, 1359.38)
bmw_e30 = Car("BMW", "E 30", "blue", 2.2, 210, 1559.38)
rolls_royce = Car()


# 3 - Acceso a atributos
# Atributos de clase: no se necesita crear un instancia:
print(Car.encendido)  # False
print(Car.num_ruedas)   # 4

# Atributos de instancia: se necesita crear una instancia
ferarri_458 = Car("Ferrari", "458 Italia", "red", 5.2, 458, 1159.38)
print(ferarri_458.manufacturer)



print("fin")
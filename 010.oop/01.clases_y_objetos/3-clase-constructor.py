# 1 - crear clase
class Car:
    # 1.1. Atributos de clase
    num_ruedas = 4
    encendido = False

    # 1.2 Método constructor
    def __init__(self, manufacturer, model, color, cc, cv, peso):
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
# Posible agregar un atributo
bmw_e30.electric = True
print(bmw_e30.manufacturer)

print(ford_mondeo)
print(tesla_model_s)
print(bmw_e30)

# 3 - Acceder a sus propiedades
print(ford_mondeo.manufacturer + " " + ford_mondeo.model + " " + ford_mondeo.color)
print(tesla_model_s.manufacturer + " " + tesla_model_s.model + " " + tesla_model_s.color)
print(bmw_e30.manufacturer + " " + bmw_e30.model + " " + bmw_e30.color)

# 4 - Modificar sus propiedades
ford_mondeo.color = "green"
print(ford_mondeo.manufacturer + " " + ford_mondeo.model + " " + ford_mondeo.color)


print("fin")
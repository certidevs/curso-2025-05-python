
keys = ("id", "manufacturer", "model", "color")
# Crea un diccionario con valores None
car = dict.fromkeys(keys)
print(type(car))
print(car)


# Crea un diccionario con valores str "Prueba"
car2 = dict.fromkeys(keys, "Prueba")
print(car2)

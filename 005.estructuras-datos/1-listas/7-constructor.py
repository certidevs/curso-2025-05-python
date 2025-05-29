
cars = list()  # Crear una lista vacía
cars2 = []
names = ['name1', 'name2']
names2 = list(('name1', 'name2'))

cars3 = list(names)  # Crear una nueva lista a partir de otra
names[0] = 'nameB'

print(names)
print(cars3)

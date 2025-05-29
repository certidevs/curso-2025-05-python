#               0       1         2       3
nominados = ["Alba", "Antoni", "Aroa", "Dani"]
print(nominados)

# append()
nominados.append("Alan")
nominados.append("Miguel")
nominados.append("Yerell")
print(nominados)


# insert()
nominados.insert(1, "Patricia")
nominados.append("Another")
print(nominados)

# Crear lista vacía y posteriormente agregar nuevos elementos
lista1 = []
for i in range(10):
    lista1.append(i)

print(lista1)
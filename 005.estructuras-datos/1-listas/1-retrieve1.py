#               0      1        2       3
nominados = ["Alba", "Antoni", "Aroa", "Dani"]
print(nominados)
print(type(nominados))
print("=======================")
for nominado in nominados:  # for each
    print(nominado)
print("=======================")
print(nominados[0])
print(nominados[1])
print(nominados[2])
print(nominados[3])
print("************************")
for i in range(len(nominados)):  # for clásico
    print(nominados[i])

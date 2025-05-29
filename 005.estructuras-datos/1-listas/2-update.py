nominados = ["Alan", "Alba", "Antoni", "Aroa", "Dani"]

# Modificar un elemento
# nominados[0] = nominados[0] + " Editado"
# nominados[0] += " Editado"

print(nominados)

for nominado in nominados:
    print()

if "Alan" in nominados:
    print("Congratulations!")

# Modificar todos los elementos
for i in range(len(nominados)):
    nominados[i] += " Editado"

print(nominados)

if "Alan" in nominados:
    print("Congratulations!")
else:
    print("False")

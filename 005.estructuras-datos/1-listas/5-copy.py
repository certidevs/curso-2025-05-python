nominados = ["Alan", "Alba", "Antoni", "Aroa", "Dani", "Evaristo", "Mario", "Leticia"]

# Forma incorrecta: esto genera una referencia, pero no una copia
nominados2 = nominados

print(nominados)
print(nominados2)
print("==========================")

# El cambio afecta a las dos 1-listas
nominados[0] = "Escopeti"
print(nominados)
print(nominados2)
print("==========================")

# Forma correcta: método copy()
nominados3 = nominados.copy()
nominados[0] = "Ricardo"

print(nominados)
print(nominados2)
print(nominados3)
print("==========================")

# Se puede utilizar también el constructor list()

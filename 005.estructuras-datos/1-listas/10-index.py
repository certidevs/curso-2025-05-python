nominados = ["Alan", "Alba", "Zacarias", "Aroa", "Dani", "Evaristo", "Mario", "Leticia", "Alan", "Alan"]

# Buscar índice de un elemento
print(nominados.index("Zacarias"))
# Buscar índice especificando desde donde comenzar
print(nominados.index("Alan", 2))
# Buscar índice especificando desde donde comenzar y terminar
print(nominados.index("Alan", 2, 9))
# Buscar índice especificando un elemento que no existe
# print(nominados.index("Tobias"))  # ValueError: 'Tobias' is not in list
nominados = ["Alan", "Alba", "Antoni", "Aroa", "Dani", "Evaristo", "Mario", "Leticia"]
print(nominados)

# 1. BORRAR UN ELEMENTO DE LA LISTA:

# 1.1 remove()
nominados.remove("Alan")
nominados.remove("Dani")
print(nominados)

# 1.2 pop() sin índice

nominados.pop()
print(nominados)

# 1.3 pop() con índice

nominados.pop(1)
print(nominados)

# 1.4 del

del nominados[1]
print(nominados)

# 2. BORRAR UNA LISTA

# 2.1 del
# del nominados
# nominados = []
# print(nominados)  # NameError

# 2.2 vaciar la lista

nominados.clear()
print(nominados)

nominados.append("Alan")
print(nominados)


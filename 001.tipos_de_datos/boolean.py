# python: snake_case
# java javascript ts: camelCase
# urls: kebab-case
# c sharp: PascalCase

# variables boolean
booleano1 = True
booleano2 = False
print(booleano1)
print(booleano2)
print(type(booleano2))

# en las comparaciones se obtiene un boolean
print(5 < 7)
booleano1 = 10 > 20
print(booleano1)

# podemos evaluar cualquier valor o variable
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#Cualquier string es True a menos que esté vacío
print(bool(""))
# Cualquier número es True a menos que sea 0
print(bool(0))
print(bool(1))

# La función predefinida isinstance devuelve boolean
x = 200
print(isinstance(x, int)) 
print(isinstance(x, float)) 
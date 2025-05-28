variable1 = "Hola mundo"
# La funcion len(x) nos permite conocer la longitud de una cadena de texto
variable2 = len(variable1)
print(variable2)

# El método strip() nos permite eliminar espacios al principio y final
variable3 = "  Texto con espacios al principio y final     "
print(variable3)
print(variable3.strip())

# El método lower() nos permite pasar un texto a minúsculas
variable3 = "TEXTO EN MAYÚSCULAS"
print(variable3.lower())

# El método upper() nos permite pasar un texto a mayúsculas
variable3 = "texto en minúsculas"
print(variable3.upper())

# El método replace() nos permite reemplazar caracteres en un texto
variable3 = "Hola Mundo"
print(variable3.replace("u", "a"))
print(variable3)
print(variable3.replace("Hola", "Adiós"))

# El método split(x) nos permite partir un texto y obtener partes del mismo
# devuelve una lista con todos los elementos que han sido separados
variable3 = "Hola, mundo, qué tal"
print(variable3.split(","))
variable3 = "Hola mundo"
print(variable3.split(" "))



text = 'honda'

for char in text:
    print(char)
    if char == 'z':
        break
else:
    print("else")  # Si se ejecuta break entonces else no se ejecuta

print("fin")

print("Hola", "mundo")
print("Hola" + " " + "mundo")

# Ejemplo real:
# Mostrar una lista de nombres []
nombres = ['nombre1', 'nombre2']

for name in nombres:
    print(name)
    
else: # actua como un finally que se ejecuta al terminar bucle salvo que rompamos el flujo:
    
    print('no hay nombres')

# print('no hay nombres')
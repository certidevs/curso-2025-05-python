# Ejemplo JavaScript
# if(50 > 10){
#
# }

check1 = 50 > 10
check2 = 20 < 100
check3 = 50 >= 50

# Estructura if
if check1 or check2:
    print("Verdadero")
    print("Verdadero2")

if check1 or (check2 and check3):
    print("Verdadero")
    print("Verdadero2")

if 5 < 10 < 20:
    print("Verdadero")

# Estructura if-else
if check1:
    print("Verdadero")
else:
    print("Falso")

# Estructura elif
if check1 or check2:
    print("Verdadero")
elif check3:
    print("Verdadero2")

# Estructura if-elif-else


if check1 or check2:
    print("Verdadero")
elif check3:
    print("Verdadero2")
else:
    print("Esto se ejecuta si no se cumple ninguna condición")

check4 = 4 > 9
# Equivalente a switch
if check1:
    print("")
elif check2:
    print("")
elif check3:
    print("")
elif check4:
    print("")
else:
    print("else")

# OPCIONAL
# if en una línea

if check1: print('Hola')

# if else en una línea (operador ternario, en Java ? :)
num1 = 40
num2 = 10
print("Verdadero") if num1 > num2 else print("Falso")

# Anidadas

if check1:
    if num1 > num2:
        print('Hello')
        if num2 > num1:
            print('')
    if num2 < num1:
        print('')

if check1:
    pass

print('Prueba pass')

print('Hola soy Evaristo')

# Sintaxis MATCH (Python 3.10+)
# Equivalente moderno al switch de otros lenguajes

def procesar_dia(dia):
    match dia:
        case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
            return "Día laboral"
        case "sábado" | "domingo":
            return "Fin de semana"
        case _:  # caso por defecto (como default en switch)
            return "Día no válido"

# Ejemplo con números
def clasificar_numero(num):
    match num:
        case 0:
            return "Cero"
        case 1 | 2 | 3:
            return "Número pequeño"
        case n if n > 10:
            return f"Número grande: {n}"
        case _:
            return "Número medio"

# Ejemplo con tipos de datos
def procesar_dato(dato):
    match dato:
        case str() if len(dato) > 5:
            return f"Cadena larga: {dato}"
        case str():
            return f"Cadena corta: {dato}"
        case int() if dato > 0:
            return f"Entero positivo: {dato}"
        case int():
            return f"Entero no positivo: {dato}"
        case list() if len(dato) > 0:
            return f"Lista con {len(dato)} elementos"
        case _:
            return "Tipo no reconocido"

# Pruebas de los ejemplos
print("\n--- Ejemplos de MATCH ---")
print(procesar_dia("lunes"))      # Día laboral
print(procesar_dia("sábado"))     # Fin de semana
print(procesar_dia("xyz"))        # Día no válido

print(clasificar_numero(0))       # Cero
print(clasificar_numero(2))       # Número pequeño
print(clasificar_numero(15))      # Número grande: 15
print(clasificar_numero(7))       # Número medio

print(procesar_dato("Hola"))      # Cadena corta: Hola
print(procesar_dato("Python es genial"))  # Cadena larga: Python es genial
print(procesar_dato(42))          # Entero positivo: 42
print(procesar_dato(-5))          # Entero no positivo: -5
print(procesar_dato([1, 2, 3]))   # Lista con 3 elementos



"""
SIMPLIFICAR EL USO DE ESTRUCTURAS CONDICIONALES COMO IF ELSE CON DICCIONARIOS:
"""
def obtener_dia_semana_ifelse(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return "Número de día inválido"

print(f"Con if/else (1): {obtener_dia_semana_ifelse(1)}")
print(f"Con if/else (5): {obtener_dia_semana_ifelse(5)}")
print(f"Con if/else (8): {obtener_dia_semana_ifelse(8)}")


def obtener_dia_semana_dict(numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo",
    }
    # Usamos .get() para proporcionar un valor por defecto si la clave no existe
    return dias_semana.get(numero, "Número de día inválido")

print(f"\nCon diccionario (1): {obtener_dia_semana_dict(1)}")
print(f"Con diccionario (5): {obtener_dia_semana_dict(5)}")
print(f"Con diccionario (8): {obtener_dia_semana_dict(8)}")


# Ejemplo con funciones como valores del diccionario
def operacion_sumar(a, b):
    return a + b

def operacion_restar(a, b):
    return a - b

def operacion_multiplicar(a, b):
    return a * b

def operacion_dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

operaciones = {
    "sumar": operacion_sumar,
    "restar": operacion_restar,
    "multiplicar": operacion_multiplicar,
    "dividir": operacion_dividir,
}

def calcular(operacion, a, b):
    # Verificamos si la operación solicitada está en nuestro diccionario
    if operacion in operaciones:
        # Obtenemos la función correspondiente
        funcion_a_ejecutar = operaciones[operacion]
        # Ejecutamos la función con los argumentos
        return funcion_a_ejecutar(a, b)
    else:
        # Manejamos el caso de una operación no válida
        return "Operación no válida"

print("\nCalculadora con diccionario:")
print(f"Sumar (5, 3): {calcular('sumar', 5, 3)}")
print(f"Restar (10, 4): {calcular('restar', 10, 4)}")
print(f"Multiplicar (6, 7): {calcular('multiplicar', 6, 7)}")
print(f"Dividir (8, 2): {calcular('dividir', 8, 2)}")
print(f"Dividir (8, 0): {calcular('dividir', 8, 0)}") # Ejemplo de división por cero
print(f"Potencia (8, 0): {calcular('potencia', 8, 0)}") # Ejemplo de operación no definida

print("\nExplicación:")
print("1. Se define un diccionario donde las claves son las condiciones y los valores son los resultados o funciones a ejecutar.")
print("2. Se usa el método .get() para buscar una clave, con un valor por defecto si no se encuentra (útil para el 'else').")
print("3. Para ejecutar funciones, se almacenan las funciones (sin paréntesis) como valores y se llaman cuando se recuperan del diccionario.")

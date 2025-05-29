# FOR-ELSE: Se ejecuta cuando el bucle termina NORMALMENTE (sin break)

# Ejemplo: Buscar un número en una lista
numeros = [1, 3, 4, 7, 9]
buscar = 4

for numero in numeros:
    if numero == buscar: # comprobar que se ha obtenido lo que querías
        print(f"¡Encontrado! {buscar}")
        break  # Si encuentra, sale del bucle. OPTIMIZACIÓN: si encontramos lo que queremos salimos
               # para evitar seguir iterando y gastar recursos
else:
    # Solo se ejecuta si NO se usó break (búsqueda fallida)
    print(f"No se encontró {buscar}")





# Caso práctico: Validar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # break implícito
    else:
        # Solo llega aquí si NO encontró divisores
        return True

print(f"7 es primo: {es_primo(7)}")   # True
print(f"8 es primo: {es_primo(8)}")   # False

# Calcular
    # si se ha entregado el trabajo y se ha obtenido nota bien break y salgo del bucle
# else
    # asignar un 0

# En otros lenguajes como java o javascript no lo hay, así que cuidado con dejarlo
# mal configurado. IMPORTANTE: depurar, establecer un break o return
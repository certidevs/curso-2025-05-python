
x = 5
k = 7
z = 10
# Operadores logicos: Los utilizamos para 
# verificar si se cumplen condiciones entre las variables
# el resultado es un valor booleano True o False

# verifica primero si x es menor que k y despues que k es menor que z
# devuelve True solo si se cumplen las dos condiciones, en caso contrario
# devuelve False
x < k and k < z

# verifica primero si x es menor que k y despues que k es menor que z
# devuelve True solo si se cumple una de lass dos condiciones
# si no se cumple ninguna entonces devuelve False
x < k or k < z

# negacion de un booleano, la comparacion x < k nos devuelve True
# al envolverlo en un not negamos ese resultado y se convierte en False
not(x < k)

# Podemos combinar los operadores logicos tantas veces 
# como queramos en una misma sentencia
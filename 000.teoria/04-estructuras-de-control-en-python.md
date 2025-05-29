---
title: 04. Estructuras de Control en Python
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/04_estructuras_de_control.ipynb).  

# Condicionales

## 1. Estructuras condicionales

Las estructuras condicionales permiten que un programa ejecute diferentes bloques de código dependiendo de si una condición es verdadera o falsa.

### a. Sintaxis básica

- **if**: Evalúa una condición. Si es verdadera, ejecuta el bloque de código asociado.
- **elif**: Se usa después de un `if` para evaluar otra condición si la primera es falsa.
- **else**: Se ejecuta si todas las condiciones anteriores son falsas.

### b. Ejemplos


```python
# Usando sólo if

edad = 18

if edad >= 18:
    print("Persona mayor de edad.")
```
> Persona mayor de edad.  


```python
# Usando if-else

edad = 18

if edad >= 18:
    print("Persona mayor de edad.")
else:
    print("Persona menor de edad.")
```
> Persona mayor de edad.  


```python
# Ejemplo completo

num = 10

if num > 5:
    print("num es mayor que 5")
elif num == 5:
    print("num es igual a 5")
else:
    print("num es menor que 5")
```
> num es mayor que 5  


### c. Anidación de estructuras condicionales

```python
lugar = "La Coruña"
llueve = True

if lugar == "La Coruña":
    if llueve:
        print("En La Coruña está lloviendo.")
    else:
        print("En La Coruña no está lloviendo.")
else:
    print("No estamos en La Coruña.")
```
> En La Coruña está lloviendo.  


---
---
	
# Bucles (while y for)

## 1. Bucle `while`

El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera. Si la condición nunca cambia a `False`, el bucle puede ser infinito.

### a. Sintaxis básica:

```python
while condición:
    # código a ejecutar mientras la condición sea verdadera
```

### b. Bucle clásico

```python
i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementamos i para evitar un bucle infinito
```
> 1  
> 2  
> 3  
> 4  
> 5  
	

Si bien esta forma de uso es correcta, casi nunca veremos algo así en Python. Más adelante veremos que existe una forma más elegante de hacer lo mismo.

### c. Bucle infinito

Otra forma común de usar `while` es mediante un bucle infinito y la sentencia `break`:


```python
while True:
    respuesta = input("Parar? (y/n)")
    if respuesta.lower() == 'y':
        print("Parando...")
        break
```
	

## 2. Bucle `for`

El bucle `for` en Python itera sobre una secuencia (como una cadena, una lista, o un rango de números).

### a. Sintaxis básica

```python
for variable in secuencia:
    # código a ejecutar en cada iteración
```

### b. Ejemplo

```python
# Imprimir cada letra de la palabra Python
for letra in "Python":
    print(letra)
```
> P  
> y  
> t  
> h  
> o  
> n  
	

## 3. Uso de `range()`

La función `range()` genera una secuencia de números y es útil cuando necesitas un rango de valores en un bucle `for`.

### a. Uso básico de `range`

En este caso, usamos `range(fin)` para generar un rango que comienza en 0 y termina en fin menos uno.

```python
# Genera los números de 0 a 4
for i in range(5):
    print(i)
```
> 0  
> 1  
> 2  
> 3  
> 4  
	

### b. Uso de `range()` definiendo inicio y fin

En este caso, usamos `range(inicio, fin)` para generar un rango que comienza desde un número específico y termina en fin menos uno.


```python
# Genera números del 5 al 9
for numero in range(5, 10):
    print(numero)
```
> 5  
> 6  
> 7  
> 8  
> 9  
	

### c. Uso de `range()` con tres parámetros (incluyendo paso)

Aquí usamos `range(inicio, fin, paso)`, lo que permite definir un paso para controlar cómo aumenta o disminuye el rango.

```python
# Genera números del 0 al 10 con un paso de 2
for numero in range(0, 11, 2):
    print(numero)
```
> 0  
> 2  
> 4  
> 6  
> 8  
> 10  
	

### d. Uso de `range()` con un rango decreciente

En este ejemplo, usamos un rango que va hacia atrás, es decir, un rango decreciente. Esto se logra usando un valor negativo para el paso.

```python
# Genera números del 10 al 1, descendiendo
for numero in range(10, 0, -1):
    print(numero)
```
> 10  
> 9  
> 8  
> 7  
> 6  
> 5  
> 4  
> 3  
> 2  
> 1  
	

### e. Uso de `range()` ignorando su valor de retorno

Existen casos en los cuales sólo nos interesa iterar algo un cierto número de veces y lo devuelvo por `range()` no nos es útil. En estos casos la convención es usar `_` como nombre de variable, y de esa forma indicar visualmente que la variable no se usará.

```python
for _ in range(4):
    print("SOS")
```
> SOS  
> SOS  
> SOS  
> SOS  
	

## 4. Combinación de estructuras de control

Es posible combinar bucles y estructuras condicionales.

### a. Ejemplo: imprimir la tabla de multiplicar de un número dado

```python
numero = int(input("Ingresa un número entero en el rango de 1 a 10"))

if 1 <= numero <= 10:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fuera de rango. Debe estar entre 1 y 10.")
```
> Tabla de multiplicar del 2:
> 	2 x 1 = 2  
> 	2 x 2 = 4  
> 	2 x 3 = 6  
> 	2 x 4 = 8  
> 	2 x 5 = 10  
> 	2 x 6 = 12  
> 	2 x 7 = 14  
> 	2 x 8 = 16  
> 	2 x 9 = 18  
> 	2 x 10 = 20  
	

---
title: 07. Funciones en Python, Parámetros y Retorno de Valores
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/07_funciones.ipynb).  
	

# Funciones en Python

## 1. Definición y uso de funciones

Una función en Python es un bloque de código reutilizable que realiza una tarea específica. Las funciones se definen usando la palabra clave `def`, seguidas por el nombre de la función y paréntesis `()`.

### a. Definición básica de una función

```python
def saludar():
    print("Hola, bienvenidos al curso de Python")
```
	
```python
# Llamar a la función
saludar()
```
> Hola, bienvenidos al curso de Python  
	

### b. Ventajas de usar funciones

Las funciones permiten:

- Reutilizar código
- Dividir un programa en partes más pequeñas y manejables
- Evitar la repetición de código
- Abstracción
	

## 2. Argumentos y parámetros

Una función puede aceptar datos (argumentos) para personalizar su comportamiento. Los parámetros se definen dentro de los paréntesis al definir la función.

### a. Ejemplo con un único argumento

```python
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")
```
	

```python
saludar_persona("Ana")
```
> Hola, Ana!  
	

```python
saludar_persona("Juan")
```
> Hola, Juan!  
	

### b. Ejemplo con múltiples argumentos

```python
def sumar(a, b):
    print(f"{a} + {b} = {a + b}")
```
	

```python
sumar(1, 2)
```
> 1 + 2 = 3  
	

```python
for a in range(10):
    sumar(1, a)
```
>  1 + 0 = 1  
>  1 + 1 = 2  
>  1 + 2 = 3  
>  1 + 3 = 4  
>  1 + 4 = 5  
>  1 + 5 = 6  
>  1 + 6 = 7  
>  1 + 7 = 8  
>  1 + 8 = 9  
>  1 + 9 = 10  
	

--- 
---

# Parámetros y retorno de valores

## 1. Parámetros por defecto

Puedes definir valores por defecto para los parámetros de una función, que se utilizarán si no se proporciona un argumento al llamar a la función.

### a. Ejemplo

```python
def saludar_persona(nombre="invitado"):
    print(f"Hola, {nombre}!")
```
	

```python
saludar_persona()  # Llama a la función sin argumentos
saludar_persona("Pedro")  # Llama a la función con un argumento
```
> Hola, invitado!  
> Hola, Pedro!  
	

## 2. Retorno de valores

Las funciones pueden devolver un valor usando la palabra clave `return`. Esto permite que el resultado de una función sea utilizado en otros cálculos o tareas.

### a. Función que devuelve un valor

```python
def sumar(a, b):
    return a + b
```
	

```python
resultado = sumar(5, 3)
print("La suma es:", resultado)
```
> La suma es: 8  
	

### b. Función con varios valores de retorno

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
```
	

```python
resultado_suma, resultado_resta = operaciones(8, 4)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")
```
> Suma: 12, Resta: 4  


## 3. Funciones con parámetros variables

A veces, es útil definir funciones que puedan recibir un número variable de argumentos usando `*args` o `**kwargs`.

### a. Ejemplo con `*args`

```python
def sumar_todos(*numeros):
    return sum(numeros)
```
	

```python
print(sumar_todos(1, 2, 3, 4))
```
> 10  
	

### b. Ejemplo con `**kwargs`

```python
def detalles_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
```
	

```python
detalles_persona(nombre="Laura", edad=25, ciudad="Galicia")
```
> nombre: Laura  
> edad: 25  
> ciudad: Galicia  
	


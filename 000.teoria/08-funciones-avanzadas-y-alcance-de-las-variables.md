---
title: 08. Funciones Avanzadas y Alcance de las Variables (Scope)
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/08_funciones_avanzadas.ipynb).  
	

# Funciones avanzadas - Argumentos y parámetros opcionales

## 1. Argumentos opcionales

En Python, puedes definir argumentos opcionales en una función estableciendo un valor por defecto para los parámetros. Si el usuario no proporciona un valor para ese argumento, se utilizará el valor por defecto.

### a. Función con argumento opcional

```python
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")
```
	

```python
saludar("Ana")  # Usa el valor por defecto para 'mensaje'
saludar("Pedro", "Buenas tardes")  # Proporciona un valor personalizado
```
>Hola, Ana!  
   Buenas tardes, Pedro!  
	

## 2. Argumentos por palabra clave

Puedes llamar a una función utilizando el nombre de los parámetros en lugar de su posición. Esto se conoce como "argumentos por palabra clave" (keyword arguments), y es útil para mejorar la legibilidad y evitar errores.

### a. Función con argumentos por palabra clave

```python
def describir_persona(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
```
	

```python
describir_persona(edad=30, ciudad="Madrid", nombre="Sofia")  # Se pueden cambiar las posiciones
```
> Nombre: Sofia, Edad: 30, Ciudad: Madrid  
	

## 3. Parámetros variables (`*args` y `**kwargs`)

Puedes usar `*args` para aceptar un número variable de argumentos posicionales y `**kwargs` para aceptar un número variable de argumentos por palabra clave.

### a. Recibir parámetros con `*args`:

```python
def sumar_numeros(*args):
    return sum(args)
```
	

```python
print(sumar_numeros(1, 2, 3, 4))
```
> 10  
	

### b. Recibir parámetros con `**kwargs`

```python
def detalles_producto(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
```
	

```python
detalles_producto(nombre="Laptop", marca="Dell", precio=1500)
```
> nombre: Laptop  
> marca: Dell  
> precio: 1500  
	

---
---

# Alcance de las Variables (Scope)

## 1. Alcance de las variables

El "alcance" o **scope** de una variable determina dónde se puede acceder a ella en el código. Python tiene dos tipos principales de alcance:

- **Local**: Las variables definidas dentro de una función solo son accesibles dentro de esa función.
- **Global**: Las variables definidas fuera de cualquier función pueden ser accesibles en todo el programa.

### a. Variables locales

```python
y = 20  # 'y' es una variable global

def otra_funcion():
    print(y)  # Accede a la variable global

otra_funcion()  # Imprime 20
```
> 20  
	

## 2. Modificar variables globales dentro de una función

Para modificar una variable global dentro de una función, se debe utilizar la palabra clave `global`.

### a. Modificación de una variable global

```python
z = 5  # Variable global

def cambiar_valor():
    global z
    z = 10  # Modifica la variable global
    print("Valor dentro de la función:", z)

cambiar_valor()  # Imprime 10
print("Valor fuera de la función:", z)  # Imprime 10
```
> Valor dentro de la función: 10  
> Valor fuera de la función: 10  
	

## 3. Alcance anidado (nonlocal)

Dentro de funciones anidadas, se puede acceder y modificar variables de la función externa usando la palabra clave `nonlocal`.

### a. Uso de `nonlocal`

```python
def funcion_externa():
    x = "local"

    def funcion_interna():
        nonlocal x
        x = "modificada"
        print("Dentro de funcion_interna:", x)

    funcion_interna()
    print("Dentro de funcion_externa:", x)

funcion_externa()
```
> Dentro de `funcion_interna`: modificada  
> Dentro de `funcion_externa`: modificada  
	

---
title: 06. Diccionarios
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/06_diccionarios.ipynb).  
	

# Diccionarios

## 1. Introducción a los diccionarios

Los diccionarios en Python son colecciones de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor asociado. Se definen usando llaves `{}`.

### a. Definición de un diccionario

```python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(mi_diccionario)
```
> `{'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}`  
	

### b. Acceso a valores

Se puede acceder a los valores de un diccionario usando la clave correspondiente.

```python
print(mi_diccionario["nombre"])  # Imprime 'Juan'
```
> Juan  
	

```python
print(mi_diccionario.get("edad"))  # Imprime '30'
```
> 30  
	

### c. Modificación de valores

Los valores en un diccionario pueden ser modificados, agregando nuevos pares clave-valor o cambiando el valor de una clave existente.

```python
mi_diccionario["edad"] = 31  # Cambia el valor asociado a la clave 'edad'
mi_diccionario["profesión"] = "Ingeniero"  # Agrega una nueva clave-valor
print(mi_diccionario)
```
> `{'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesión': 'Ingeniero'}`  
	

### d. Métodos más usados de los diccionarios

- **`keys()`**: Devuelve las claves del diccionario.
- **`values()`**: Devuelve los valores del diccionario.
- **`items()`**: Devuelve los pares clave-valor como tuplas.
- **`pop()`**: Elimina una clave y su valor asociado.

```python
print(mi_diccionario.keys())  # Devuelve las claves
```
> ` dict_keys(['nombre', 'edad', 'ciudad', 'profesión'])`  
	

```python
print(mi_diccionario.values())  # Devuelve los valores
```
> `dict_values(['Juan', 31, 'Madrid', 'Ingeniero'])`  
	

```python
mi_diccionario.pop("ciudad")  # Elimina el par clave-valor con clave 'ciudad'
print(mi_diccionario)
```
> `{'nombre': 'Juan', 'edad': 31, 'profesión': 'Ingeniero'}`  
	

---
---

# Manipulación de estructuras de datos

## 1. Rebanado de listas y tuplas

El rebanado (_slicing_) permite acceder a una porción de una lista o tupla utilizando el operador `:`.

### a. Operaciones de rebanado en listas

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:5])  # Imprime los elementos de índice 2 a 4: [2, 3, 4]
```
> `[2, 3, 4]`  
	

```python
print(numeros[:4])  # Imprime los primeros cuatro elementos: [0, 1, 2, 3]
```
> `[0, 1, 2, 3]`  
	

```python
print(numeros[5:])  # Imprime desde el índice 5 hasta el final: [5, 6, 7, 8, 9]
```
> `[5, 6, 7, 8, 9]`  
	

```python
print(numeros[::2])  # Imprime los elementos con un salto de 2: [0, 2, 4, 6, 8]
```
> `[0, 2, 4, 6, 8]`  
	

## 2. Comprensión de listas

La comprensión de listas es una manera concisa de crear listas a partir de secuencias o condiciones, y puede reemplazar bucles `for` tradicionales.

### a. Ejemplo básico de comprensión de listas:

```python
cuadrados = [x**2 for x in range(10)]  # Crea una lista de los cuadrados de 0 a 9
print(cuadrados)
```
> `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`  
	

### b. Comprensión de listas con condiciones

```python
pares = [x for x in range(10) if x % 2 == 0]  # Crea una lista con los números pares
print(pares)
```
> `[0, 2, 4, 6, 8]`  
	

## 3. Manipulación de diccionarios

Puedes iterar sobre los pares clave-valor de un diccionario, aplicar condiciones, o crear nuevos diccionarios con comprensión de diccionarios.

### a. Ejemplo de iteración sobre diccionarios

```python
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
```
> nombre: Juan  
> edad: 31  
> profesión: Ingeniero  
	

### b. Comprensión de diccionarios

```python
nombres = {"Juan": 30, "Ana": 25, "Luis": 35}
nombres_mayores_30 = {clave: valor for clave, valor in nombres.items() if valor > 30}
print(nombres_mayores_30)  # Imprime {'Luis': 35}
```
> `{'Luis': 35}`  
	

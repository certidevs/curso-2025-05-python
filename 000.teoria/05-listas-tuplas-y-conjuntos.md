---
title: 05. Listas, Tuplas y Conjuntos
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/05_listas_tuplas_y_conjuntos.ipynb).  
	

# Listas

## 1. Introducción a las listas

Las listas en Python son colecciones ordenadas y mutables, lo que significa que puedes modificar sus elementos después de haberlas creado. Se definen usando corchetes `[]`.

### a. Definición de una lista

```python
frutas = ["manzana", "banana", "cereza"]
print(frutas)
```
> `['manzana', 'banana', 'cereza']`  

### b. Acceso y modificación de elementos

Puedes acceder a los elementos de una lista mediante su índice, y modificar los elementos directamente.

```python
print(frutas[1])  # Acceso al segundo elemento: 'banana'
frutas[1] = "mango"  # Cambia 'banana' por 'mango'
print(frutas)
```
> banana  
> `['manzana', 'mango', 'cereza']`  
	
### c. Métodos comunes de las listas

Algunos métodos útiles de las listas incluyen:

- **`append()`**: Agrega un elemento al final de la lista.
- **`insert()`**: Inserta un elemento en una posición específica.
- **`remove()`**: Elimina el primer elemento que coincide con el valor.
- **`pop()`**: Elimina el elemento en una posición específica (por defecto, el último).
- **`sort()`**: Ordena los elementos de la lista.

#### Ejemplos

```python
frutas.append("naranja")  # Agrega 'naranja' al final
print(frutas)
```
> `['manzana', 'mango', 'cereza', 'naranja']`  
	

```python
frutas.insert(1, "kiwi")  # Inserta 'kiwi' en la posición 1
print(frutas)
```
> `['manzana', 'kiwi', 'mango', 'cereza', 'naranja']`  
	

```python
frutas.remove("manzana")  # Elimina 'manzana'
print(frutas)
```
> `['kiwi', 'mango', 'cereza', 'naranja']`  
	

```python
ultima_fruta = frutas.pop()  # Elimina el último elemento y lo guarda
print("Última fruta eliminada:", ultima_fruta)
print(frutas)
```
> `Última fruta eliminada: naranja`  
> `['kiwi', 'mango', 'cereza']`  
	

```python
frutas.sort()  # Ordena la lista alfabéticamente
print(frutas)
```
> `['cereza', 'kiwi', 'mango']`  
	

### d. Listas anidadas

Las listas pueden contener otras listas, lo que se llama listas anidadas.

```python
lista_anidada = [["manzana", "banana"], ["zanahoria", "pepino"]]
print(lista_anidada[0])  # Acceso a la primera sublista
print(lista_anidada[1][1])  # Acceso a 'pepino'
```
> `['manzana', 'banana']`  
> pepino  

### e. Iterar una lista con `for`

Puedo recorrer todos los elementos de una lista mediante el uso de `for`

```python
for fruta in ["banana", "manzana", "pera"]:
    print(f"{fruta=}")
```
> fruta='banana'  
> fruta='manzana'  
> fruta='pera'  
	
### f. Obtener el índice de los elementos de la lista al iterar con `for`

Si además de los elementos de una lista, necesito también sus índices, puedo usar la función `enumerate()` 

```python
for indice, fruta in enumerate(["banana", "manzana", "pera"]):
    print(f"{indice}. {fruta}")
```
> `0. banana`  
> `1. manzana`  
> `2. pera`  
	

---
---

# Tuplas y conjuntos

## 1. Tuplas

Las tuplas son similares a las listas, pero a diferencia de estas, son inmutables (no se pueden modificar una vez creadas). Se definen usando paréntesis `()`.

### a. Definición de una tupla

```python
mi_tupla = ("manzana", "banana", "cereza")
print(mi_tupla)
```
> `('manzana', 'banana', 'cereza')`  
	
### b. Acceso a elementos en una tupla

Puedes acceder a los elementos de una tupla de la misma manera que en las listas, usando índices, pero no puedes modificar sus elementos.

```python
print(mi_tupla[1])  # Acceso al segundo elemento: 'banana'

# Intentar modificar un elemento dará un error:
# mi_tupla[1] = "mango"  # Esto generará un TypeError
```
> banana  
	
### c. Conversión de tuplas a listas

Si necesitas modificar una tupla, puedes convertirla temporalmente a una lista, hacer los cambios y volver a convertirla en tupla.

```python
mi_lista = list((1, 2, 3))  # Convertir tupla a lista
mi_lista[1] = "mango"  # Modificar la lista
mi_tupla = tuple(mi_lista)  # Convertir lista de nuevo a tupla
print(mi_tupla)
```
> `(1, 'mango', 3)`  
	

## 2. Conjuntos

Los conjuntos son colecciones desordenadas y no permiten elementos duplicados. Se definen usando llaves `{}` o la función `set()`.

### a. Definición de un conjunto

```python
mi_conjunto = {"manzana", "banana", "cereza"}
print(mi_conjunto)
```
> `{'cereza', 'banana', 'manzana'}`  
	

### b. Métodos más usados en conjuntos

Los conjuntos permiten operaciones como:

- **`add()`**: Agrega un elemento al conjunto.
- **`remove()`**: Elimina un elemento del conjunto (genera un error si no existe).
- **`discard()`**: Elimina un elemento del conjunto (no genera error si no existe).
- **`union()`**: Une dos conjuntos.
- **`intersection()`**: Devuelve los elementos comunes entre dos conjuntos.
- **`difference()`**: Devuelve los elementos que están en el primer conjunto pero no en el segundo.

#### Ejemplos

```python
mi_conjunto.add("naranja")  # Agrega 'naranja' al conjunto
print(mi_conjunto)
```
> `{'cereza', 'banana', 'naranja', 'manzana'}`  
	

```python
mi_conjunto.remove("banana")  # Elimina 'banana' del conjunto
print(mi_conjunto)
```
> `{'cereza', 'naranja', 'manzana'}`  
	

```python
# Conjuntos para realizar operaciones:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A.union(B)  # Unión de A y B
print("Unión:", union)
```
> `Unión: {1, 2, 3, 4, 5, 6}`  
	

```python
interseccion = A.intersection(B)  # Intersección de A y B
print("Intersección:", interseccion)
```
> `Intersección: {3, 4}`  
	

```python
diferencia = A.difference(B)  # Elementos en A que no están en B
print("Diferencia:", diferencia)
```
> `Diferencia: {1, 2}`  
	


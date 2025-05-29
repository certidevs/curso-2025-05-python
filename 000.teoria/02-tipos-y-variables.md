---
title: 02. Tipos y variables
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/02_tipos_y_variables.ipynb).
	

# Tipos de datos en Python

## 1. Tipos de datos básicos

Python tiene varios tipos de datos básicos. A continuación, se describen los más comunes:

  - **Enteros (int)**: Números enteros, positivos o negativos, sin decimales. Ejemplo: `42`, `-3`.
    
  - **Flotantes (float)**: Números reales, que pueden incluir decimales. Ejemplo: `3.14`, `-0.001`.
    
  - **Cadenas (str)**: Secuencias de caracteres que se utilizan para representar texto. Las cadenas se pueden definir con comillas simples o dobles. Ejemplo: `'Hola, mundo!'`, `"Python es genial!"`.
    
  - **Booleanos (bool)**: Representan valores de verdad. Solo pueden ser `True` o `False`.

### a. Ejemplos


```python
type(10)
```
> int  


```python
type(3.14)
```
> float  


```python
print("hola mundo")
```
> hola mundo  


```python
print('hola', type('hola'))
```
> `hola <class 'str'>`  


```python
print(True, type(True), False, type(False))
```
> `True <class 'bool'> False <class 'bool'>`  


### b. Conversión de tipos

Es posible convertir entre diferentes tipos de datos utilizando funciones integradas, como:

- `int()`: Convierte un valor a entero.
- `float()`: Convierte un valor a flotante.
- `str()`: Convierte un valor a cadena.

#### Ejemplos

```python
type(int("100"))
```
> int  


```python
type(float("100"))
```
> float  


```python
type(str(100))
```
> str  
	

---
---

# Variables y asignación

## 1. ¿Qué es una variable?

Una variable es un espacio en la memoria que se utiliza para almacenar datos. En Python, no es necesario declarar el tipo de variable antes de usarla, ya que Python utiliza tipado dinámico.

## 2. Asignación de variables

Para asignar un valor a una variable, se utiliza el operador `=`. La sintaxis es la siguiente:

```python
nombre_variable = valor
```

### a. Ejemplo de asignación de variables


```python
# Variable de tipo int
num = 10
```
	

```python
# Para ver el valor de la variable podemos usar print
print(num)
```
> 10  



```python
# Variable de tipo str
nombre = "Lucas"
print(nombre)
```
> Lucas  



```python
# Variable de tipo bool
en_ejecucion = True
print(en_ejecucion, type(en_ejecucion))
```
> `True <class 'bool'>`  


### b. Nombres de variables

Los nombres de las variables deben seguir ciertas reglas:

- Pueden contener letras, números y guiones bajos (`_`).
  
- No pueden comenzar con un número.
  
- No pueden contener espacios ni caracteres especiales.
  
- No pueden ser palabras reservadas de Python (como `if`, `for`, `while`, etc.).
  
- Minúsculas y mayúsculas son diferentes, aunque no se usa mayúsculas para variables (ver pep8).

### c. Nombres válidos de variables

```python
x_ = 10
```
	
```python
y0 = 4.9
```
	
```python
_zen_de_python = "Simple es mejor que complejo"
```
	
```python
CONSTANTE = 100
```
	

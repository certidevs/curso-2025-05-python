---
title: 03. Operadores en Python
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/02_tipos_y_variables.ipynb).  
	

# Operadores aritméticos y lógicos

## 1. Operadores aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas comunes como suma, resta, multiplicación, etc.

| Operador | Operación                                   | Ejemplo  |
| -------- | ------------------------------------------- | -------- |
| `+`      | Suma                                        | `x + y`  |
| `-`      | Resta                                       | `x - y`  |
| `*`      | Multiplicación                              | `x * y`  |
| `/`      | División (devuelve un valor `float`)        | `x / y`  |
| `//`     | División entera (descarta la parte decimal) | `x // y` |
| `%`      | Módulo (devuelve el resto de la división)   | `x % y`  |
| `**`     | Potencia                                    | `x ** y` |

### a. Python como una calculadora

```python
# Suma
10 + 5
```
> 15  

```python
# Resta
1 - 0.1
```
> 0.9  

```python
# Multiplicación
10 * 2
```
> 20  

```python
# División
2 / 3
```
> 0.6666666666666666  

```python
# División entera
10 // 3
```
> 3  

```python
# Módulo (resto de la división)
9 % 2
```
> 1  

```python
# Exponente
3 ** 2
```
> 9  
	

### b. Uso de variables

```python
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Exponente:", a ** b)
```
> Suma: 13  
> Resta: 7  
> Multiplicación: 30  
> División: 3.3333333333333335  
> División entera: 3  
> Módulo: 1  
> Exponente: 1000  
	

## 2. Operadores lógicos

### Operadores lógicos

Los operadores lógicos permiten realizar operaciones que resultan en valores booleanos (`True` o `False`).

- **and**: Devuelve `True` si ambas condiciones son verdaderas.
- **or**: Devuelve `True` si al menos una de las condiciones es verdadera.
- **not**: Devuelve `True` si la condición es falsa y viceversa.

#### a. Pruebas booleanas

```python
True and True
```
> True  

```python
True and False
```
> False  

```python
True or True
```
> True  

```python
True or False
```
> True  

```python
not True
```
> False  

```python
not False
```
> True  

#### b. Uso de variables

```python
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
```
> x and y: False  
> x or y: True  
> not x: False  
	

---
---
# Operadores de comparación

## 1. Operadores de comparación

Los operadores de comparación evalúan dos valores y devuelven `True` o `False` según la condición.

- **Igual a (`==`)**: Verifica si dos valores son iguales.
  
- **Distinto de (`!=`)**: Verifica si dos valores son diferentes.
  
- **Mayor que (`>`)**: Verifica si el valor de la izquierda es mayor que el de la derecha.
  
- **Menor que (`<`)**: Verifica si el valor de la izquierda es menor que el de la derecha.
  
- **Mayor o igual que (`>=`)**: Verifica si el valor de la izquierda es mayor o igual que el de la derecha.
  
- **Menor o igual que (`<=`)**: Verifica si el valor de la izquierda es menor o igual que el de la derecha.

### a. Uso con variables

```python
a = 5
b = 10

print("a == b:", a == b)  # Devuelve False
print("a != b:", a != b)  # Devuelve True
print("a > b:", a > b)  # Devuelve False
print("a < b:", a < b)  # Devuelve True
print("a >= b:", a >= b)  # Devuelve False
print("a <= b:", a <= b)  # Devuelve True
```
> a == b: False  
> a != b: True  
> a > b: False  
> a < b: True  
> a >= b: False  
> a <= b: True  
	

## 2. Uso combinado de operadores

En Python, puedes combinar operadores para crear expresiones más complejas. Las expresiones lógicas pueden contener operadores de comparación y aritméticos.

### a. Ejemplo de uso combinado de operadores aritméticos, lógicos y de comparación

```python
x = 20
y = 15
z = 10

resultado = (x > y) and (y > z)  # Devuelve True
print("Resultado:", resultado)

resultado_2 = (x + z > y) or (z - y > x)  # Devuelve True
print("Resultado 2:", resultado_2)
```
> Resultado: True  
> Resultado 2: True  

### b. Precedencia de operadores en Python

En Python, los operadores de comparación y lógicos tienen un **orden de precedencia** que determina cómo se evalúan en expresiones complejas. Conocer este orden es fundamental para evitar errores lógicos en los programas.

1. **Paréntesis `()`** – Agrupan expresiones para modificar la precedencia.
   
2. **Exponenciación `**`** – Tiene la mayor precedencia después de los paréntesis.
   
3. **Negación `-` (unario)**
   
4. **Multiplicación `*`, División `/`, División entera `//`, Módulo `%`
   
5. **Suma `+`, Resta `-`**
   
6. **Operadores de comparación** (`<`, `<=`, `>`, `>=`, `==`, `!=`)
   
7. **Operadores lógicos**:
   - **NOT** (`not`) – Negación lógica (precedencia más alta entre lógicos).
   - **AND** (`and`) – Evaluación lógica condicional.
   - **OR** (`or`) – Evaluación lógica condicional (precedencia más baja).

#### Ejemplos

```python
x = 5
y = 10
z = 15
```
	
```python
result = x < y and y < z  # True, se evalúa de izquierda a derecha
print(result)
```
> True  

```python
print(x < y < z) # Pythonic
```
> True  

```python
result = not (x < y and y < z)  # False, se niega el resultado final
print(result)
```
> False  

```python
result = x + 2 * y > z # True, primero se evalúa la multiplicación (2 * y), luego la suma
print(result)
```
> True  

```python
result = (x + 2) * y > z  # True, paréntesis altera la precedencia
print(result)
```
> True  
	

---
title: 13. Anexo I
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/13_anexo.ipynb).  
	

## Uso de la función `print()` y f-strings

La función `print()` en Python es fundamental para mostrar información en la consola. A continuación, exploraremos los detalles sobre cómo usarla, incluyendo ejemplos prácticos. Además, veremos cómo el uso de **f-strings** pueden ser una manera más eficiente de formatear cadenas de texto en Python.

### 1. Función `print()`

La función `print()` se utiliza para mostrar uno o más valores en la consola. Puedes pasar diferentes tipos de datos como argumentos: cadenas de texto, números, listas, etc. Esta función imprime los valores separados por un espacio, a menos que se indique lo contrario.

#### Sintaxis básica:

```python
print(valor1, valor2, ..., sep=' ', end='\n')
```

- **valor1, valor2, ...**: Los valores que deseas imprimir.
- **sep**: El separador entre los valores, por defecto es un espacio (`' '`).
- **end**: Lo que se imprime al final de la salida, por defecto es un salto de línea (`'\n'`).

#### Ejemplos:

```python
# Imprimir un solo valor
print("Hola, mundo")
```
> Hola, mundo  
	

```python
# Imprimir varios valores con el separador por defecto (espacio)
print("Python", "es", "genial")
```
> Python es genial  

```python
# Usar sep para cambiar el separador
print("Python", "es", "genial", sep="-")
```
> Python-es-genial  
	

```python
# Usar end para cambiar cómo termina la línea
print("Primera línea", end=" ")
print("Segunda línea")
```
> Primera línea Segunda línea  
	

### 2. Imprimir con variables

Es posible imprimir valores de variables directamente con la función `print()`. Los valores pueden ser de cualquier tipo: cadenas, números, listas, etc.

```python
nombre = "Ana"
edad = 25
print("Mi nombre es", nombre, "y tengo", edad, "años.")
```
> Mi nombre es Ana y tengo 25 años.  
	

### 3. Uso de f-strings

Las **f-strings** son una forma moderna y eficiente de formatear cadenas en Python. Introducidas en Python 3.6, permiten incluir variables o expresiones dentro de una cadena usando llaves `{}`. Son más simples que las alternativas anteriores como `str.format()` y el operador `%`.

#### Sintaxis básica de f-strings:

```python
f"texto {variable} texto"
```
	
#### Ejemplos:

```python
nombre = "Carlos"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")
```
> Mi nombre es Carlos y tengo 30 años.  
	

### 4. Evaluar expresiones dentro de f-strings

Con f-strings, no solo puedes insertar variables, sino también evaluar expresiones directamente dentro de las llaves `{}`.

```python
x = 10
y = 5
print(f"La suma de {x} + {y} es {x + y}")
```
> La suma de 10 + 5 es 15  
	

### 5. Especificar formato en f-strings

f-strings también permiten aplicar formato a los valores. Esto es útil cuando trabajas con números decimales, alineación de texto, etc.

#### Ejemplo de formato numérico:

```python
pi = 3.1415926535
print(f"El valor de pi es {pi:.2f}")
```
> El valor de pi es 3.14  
	

#### Ejemplo de alineación y relleno:

```python
nombre = "Carlos"

# Alinear a la derecha en un espacio de 10 caracteres
print(f"{nombre:>10}")

# Alinear a la izquierda
print(f"{nombre:<10}")

# Alinear al centro
print(f"{nombre:^10}")
```
>         Carlos  
>     Carlos    
>       Carlos  
	



### 6. Combinar `print()` y f-strings

Combinar la función `print()` con f-strings permite construir mensajes dinámicos de forma eficiente.

```python
nombre = "Lucía"
edad = 28
ciudad = "Madrid"
print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}.")
```
> Hola, soy Lucía, tengo 28 años y vivo en Madrid.
	

#### Uso con diccionarios

Puedes acceder a los valores de un diccionario dentro de una f-string.

```python
persona = {"nombre": "Lucía", "edad": 25}
mensaje = f"{persona['nombre']} tiene {persona['edad']} años."
print(mensaje)
```
> Lucía tiene 25 años.
	

### 7. Llamadas a funciones dentro de f-strings

Es posible ejecutar funciones dentro de las llaves `{}` para mostrar el resultado.

```python
def cuadrado(n):
    return n * n

valor = 5
print(f"El cuadrado de {valor} es {cuadrado(valor)}.")
```
> El cuadrado de 5 es 25.


---

## Uso de la función `input()`

La función `input()` permite que el usuario ingrese datos desde la consola. La función detiene la ejecución del programa y espera a que el usuario escriba algo y presione Enter. El valor retornado por `input()` siempre será de tipo **cadena de texto** (_string_), por lo que, si se espera un número, será necesario convertirlo usando funciones como `int()` o `float()`.

#### Sintaxis básica:

```python
input(prompt)
```

- **prompt**: Es un texto opcional que se mostrará en la consola antes de que el usuario ingrese algo, normalmente para dar instrucciones o hacer una pregunta.

#### Ejemplos:

```python
# Solicitar un nombre al usuario
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")
```
	

```python
# Solicitar un número y convertirlo a entero
edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")
```

> **Nota**: Es importante recordar que los valores ingresados por `input()` son cadenas, por lo que si se necesitas realizar operaciones numéricas, es necesario convertir esos valores.
	

### Resumen de uso combinado de `print()`, `input()` y f-strings

Estas tres herramientas básicas se usarán a lo largo del curso para interactuar con el usuario, obtener datos y mostrarlos de manera formateada.

#### Ejemplo completo:

```python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿Dónde vives? ")

print(f"Hola, {nombre}. Tienes {edad} años y vives en {ciudad}.")
```
	

---

## Estilo de Código - PEP8

[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

#### ¿Qué es PEP?

PEP (_Python Enhancement Proposal_) es un documento que describe nuevas características, mejoras o guías relacionadas con Python. Estos documentos son fundamentales para la evolución del lenguaje, ya que proponen y detallan cómo implementar ciertas funcionalidades.
	

#### ¿Qué es PEP8?

[PEP8](https://peps.python.org/pep-0008/) es una de las guías más importantes dentro de la comunidad Python. Establece convenciones de estilo para escribir código Python de manera clara, legible y consistente. Aunque no es obligatorio seguir PEP8, es altamente recomendable, especialmente cuando se trabaja en proyectos colaborativos.
	

#### Importancia de PEP8

- Legibilidad: Ayuda a que el código sea más fácil de leer y comprender, tanto para ti como para otros programadores.
  
- Mantenimiento: Facilita el mantenimiento del código a lo largo del tiempo, ya que un código claro y bien estructurado es más sencillo de actualizar.
  
- Consistencia: Garantiza que todos los programadores sigan las mismas reglas de estilo, lo que es especialmente importante en proyectos en equipo o grandes aplicaciones.

Algunos puntos clave de PEP8 incluyen:

- Indentación: Usar 4 espacios por nivel de indentación.
  
- Líneas de longitud: Las líneas no deben exceder los 79 caracteres.
  
- Espaciado: Manejar los espacios en blanco de manera coherente alrededor de operadores y después de comas.
  
- Nombres de variables y funciones: Utilizar `snake_case` para nombres de variables y funciones, y `CamelCase` para nombres de clases.

Seguir PEP8 contribuye a un código más limpio y fácil de compartir entre desarrolladores, promoviendo las mejores prácticas en la comunidad Python.
	

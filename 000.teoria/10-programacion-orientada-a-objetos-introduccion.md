---
title: 10. Programación Orientada a Objetos (OOP) - Introducción
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/10_programacion_orientada_a_objetos.ipynb).  
	

## 1. Conceptos básicos de la Programación Orientada a Objetos (OOP)

La **Programación Orientada a Objetos (OOP)** es un paradigma de programación que se basa en la creación de objetos para representar entidades del mundo real o abstracto. A través de este enfoque, el código se estructura de manera más clara, reutilizable y mantenible.
	
### a. Elementos clave de la OOP

- **Clase**: Es una plantilla o _blueprint_ que define las características (atributos) y comportamientos (métodos) de los objetos que se crearán a partir de ella.
  
- **Objeto**: Es una instancia de una clase, que contiene valores específicos de los atributos definidos en la clase.
  
- **Atributos**: Son las propiedades o datos asociados a una clase. Pueden ser atributos de instancia (específicos para cada objeto) o atributos de clase (compartidos entre todas las instancias).
  
- **Métodos**: Son funciones dentro de una clase que definen las acciones o comportamientos que los objetos pueden realizar.
	

### b. Definición de una clase y creación de un objeto

La estructura básica de una clase en Python se define con la palabra clave `class`:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

# Creación de un objeto (instancia) de la clase Persona
persona1 = Persona("Carlos", 30)

# Accediendo a los atributos del objeto
print(persona1.nombre)  # Salida: Carlos
print(persona1.edad)    # Salida: 30
```
> Carlos  
> 30  

En el ejemplo anterior:
- `Persona` es la clase.
- `persona1` es un objeto (instancia) de la clase `Persona`.
- `__init__` es el **constructor**, un método especial que se ejecuta automáticamente al crear un objeto. Se usa para inicializar los atributos del objeto.
	

### c. Importancia de la OOP

La OOP permite estructurar el código de manera que sea fácil de entender, modificar y reutilizar. Sus principales ventajas son:

- **Encapsulación**: Los atributos y métodos se agrupan en una clase, facilitando la organización del código.
  
- **Herencia**: Permite que una clase herede propiedades y comportamientos de otra clase.
  
- **Polimorfismo**: Permite que objetos de diferentes clases puedan ser tratados de manera uniforme, siempre y cuando compartan ciertos comportamientos.
	

---

# Atributos y métodos

## 1. Atributos de instancia y atributos de clase

Los atributos pueden ser de dos tipos:

- **Atributos de instancia**: Son únicos para cada objeto creado a partir de una clase. Cada instancia de una clase puede tener valores distintos en estos atributos.
  
- **Atributos de clase**: Son compartidos por todas las instancias de la clase.
	

### a. Atributos de instancia

```python
class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre   # Atributo de instancia
        self.puesto = puesto   # Atributo de instancia
        self.salario = salario # Atributo de instancia
```
	

```python
# Crear dos objetos de la clase Empleado
empleado1 = Empleado("Luis", "Desarrollador", 5000)
empleado2 = Empleado("Ana", "Gerente", 6000)
```
	

```python
# Acceder a los atributos de cada objeto
print(empleado1.nombre, empleado1.puesto, empleado1.salario)
print(empleado2.nombre, empleado2.puesto, empleado2.salario)
```
> Luis Desarrollador 5000  
> Ana Gerente 6000  
	

En este ejemplo, cada empleado tiene sus propios valores para `nombre`, `puesto` y `salario`, que son atributos de instancia.
	

### b. Atributos de clase

Los atributos de clase son aquellos que son compartidos por todas las instancias de una clase. Pueden ser útiles para almacenar información común entre todos los objetos.

```python
class Empresa:
    sector = "Tecnología"  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia
```
	

```python
# Crear dos objetos de la clase Empresa
empresa1 = Empresa("InnovaTech")
empresa2 = Empresa("SoftSolutions")
```
	

```python
# Acceder a los atributos de clase
print(empresa1.sector, empresa2.sector)

# Acceder a los atributos de instancia
print(empresa1.nombre, empresa2.nombre)
```
> Tecnología Tecnología  
> InnovaTech SoftSolutions  
	

## 2. Métodos

Los **métodos** son funciones que pertenecen a una clase y permiten a los objetos de esa clase realizar acciones o comportamientos específicos. Los métodos se definen dentro de la clase, y el primer parámetro de un método siempre es `self`, que representa al objeto que está llamando al método.

### a. Métodos de instancia

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")
```
	

```python
persona = Persona("Ana")
persona.saludar()
```
> Hola, me llamo Ana  
	

### b. Método con parámetros adicionales

Los métodos también pueden aceptar parámetros adicionales que permiten realizar acciones más flexibles.

```python
class Cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad  # Capacidad máxima de la cafetera en mililitros

    def preparar_cafe(self, cantidad):
        if cantidad > self.capacidad:
            print(f"No se puede preparar {cantidad}ml. La capacidad máxima es {self.capacidad}ml.")
        else:
            print(f"Preparando {cantidad}ml de café...")
```
	

```python
# Crear una instancia de la clase Cafetera con una capacidad de 1000ml
mi_cafetera = Cafetera(1000)
```
	

```python
# Llamar al método preparar_cafe con un argumento no opcional
mi_cafetera.preparar_cafe(500)  # Preparando 500ml de café...
mi_cafetera.preparar_cafe(1200) # No se puede preparar 1200ml. La capacidad máxima es 1000ml.
```
> Preparando 500ml de café...  
> No se puede preparar 1200ml. La capacidad máxima es 1000ml.  
	

## 3. Atributos y métodos privados

En Python, los atributos y métodos pueden ser "privados", lo que significa que no deberían ser accesibles directamente fuera de la clase. Para hacer que un atributo o método sea privado, se utiliza un guion bajo doble `__` antes del nombre.

### a. Atributo privado

```python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    # Método para consultar el saldo
    def consultar_saldo(self):
        return self.__saldo

    # Método para depositar dinero
    def depositar(self, monto):
        self.__saldo += monto
```
	

```python
# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(1000)
```
	

```python
# Consultar el saldo mediante el método
print("Saldo inicial:", cuenta.consultar_saldo())
```
> Saldo inicial: 1000  
	

```python
# Intentar acceder al atributo privado directamente causará un error
try:
    print(cuenta.__saldo)  # Esto producirá un AttributeError
except AttributeError as e:
    print(e)
```
>  `'CuentaBancaria' object has no attribute '__saldo'`  
	

En este ejemplo, `__saldo` es un atributo privado, por lo que no se puede acceder a él directamente desde fuera de la clase. Sin embargo, se puede acceder a él a través del método público `consultar_saldo()`.
	


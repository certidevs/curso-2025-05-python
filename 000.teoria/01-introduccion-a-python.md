---
title: 01. Introducción a Python
---
# Conceptos generales de Python

## 1. ¿Qué es Python?

**Python** es un lenguaje de programación de alto nivel, interpretado y de propósito general, que se destaca por su simplicidad y legibilidad. 

Es de código abierto y fue creado por Guido van Rossum y lanzado por primera vez en 1991.

### a. Características generales

- **Interpretado**: Python ejecuta el código línea por línea, lo que significa que no necesita ser compilado previamente como otros lenguajes de programación. Esto facilita la **prueba rápida de código** y el **desarrollo ágil**, ya que los errores pueden identificarse y corregirse en tiempo real.

- **Código abierto**: Python es un lenguaje de **código abierto** o **open source**, lo que permite que su código fuente esté disponible públicamente. Esto significa que cualquier persona puede utilizar, modificar y distribuir Python sin restricciones, lo que fomenta una **comunidad activa y colaborativa** que contribuye continuamente a su mejora y expansión.

- **Multiparadigma**: Python es **multiparadigma**, lo que significa que soporta varios enfoques o estilos de programación, como:
  - **Programación orientada a objetos (OOP)**: Basada en la creación de objetos que contienen datos y métodos para operar sobre esos datos.
  - **Programación estructurada o imperativa**: Se enfoca en el uso de estructuras de control como bucles y condicionales para gestionar el flujo del programa.
  - **Programación funcional**: Permite tratar funciones como objetos de primera clase y aprovechar técnicas como funciones anónimas, inmutabilidad y recursión.
  
  Aunque se destaca por su enfoque en la **orientación a objetos**, su flexibilidad permite que los desarrolladores elijan el estilo que mejor se adapte a sus necesidades.

- **Lenguaje de alto nivel**: Python es un lenguaje de **alto nivel**, lo que significa que está más cercano al lenguaje humano que al lenguaje máquina. Esto hace que sea **más fácil de aprender** y **más intuitivo**, ya que sus sentencias se parecen al inglés. Al estar abstraído de los detalles del hardware, los programadores pueden concentrarse más en resolver problemas lógicos que en gestionar la complejidad técnica del sistema.

Este conjunto de características hace que Python sea una excelente opción tanto para principiantes como para desarrolladores experimentados, ya que combina **simplicidad** y **potencia** en un solo lenguaje.
	

## 2. ¿Para qué se usa Python?

Python es utilizado en una amplia variedad de campos:

- **Desarrollo web** (con frameworks como Django y Flask)
  
- **Ciencia de datos y aprendizaje automático** (con bibliotecas como Pandas, NumPy, TensorFlow)
  
- **Automatización** y scripts
  
- **Desarrollo de videojuegos**
  
- **Aplicaciones de escritorio** y más.
	

### 3. Historia y evolución de Python
- Creado a fines de los 80 por Guido van Rossum, inspirado en lenguajes como ABC.
- Python ha pasado por varias versiones importantes, siendo la transición de Python 2 a Python 3 (en 2008) un momento clave en su evolución.
	

---
---
# Formas de ejecutar Python y el entorno de trabajo (Google Colab)

## 1. Ejecución de Python

Existen diferentes formas de ejecutar un programa en Python:

### a. Ejecutar Python en la terminal (modo interactivo)

Puedes abrir la terminal en tu sistema operativo y simplemente escribir `python` para entrar en el modo interactivo. Esto permite ejecutar líneas de código inmediatamente y ver los resultados.

- Ventajas: 
  - Es rápido y directo.
  - Útil para probar fragmentos de código.

### b. Usar un IDE (Entorno de Desarrollo Integrado)

Existen varios IDEs para Python, como PyCharm, VSCode o Sublime Text. Estos entornos ofrecen herramientas avanzadas para escribir, depurar y ejecutar código.

- Ventajas: 
  - Herramientas avanzadas como autocompletado y depuración.
  - Ideal para grandes proyectos.

- Desventajas: 
  - Requiere instalación y configuración.
  
### c. Uso de Notebooks Interactivos (Jupyter Notebooks)

Un [Jupyter Notebook](https://jupyter.org/) permite escribir y ejecutar código en "celdas", y es muy utilizado en investigación y enseñanza.

- Ventajas:
  - Permite incluir y compartir código, texto, gráficos, todo en el mismo documento.
  - Ideal para la exploración de datos, visualización y experimentos interactivos.

## 2. Google Colab - El entorno que usaremos

### a. ¿Qué es Google Colab?

Google Colab es un entorno basado en la nube que permite ejecutar Jupyter Notebooks sin la necesidad de instalar nada en tu computadora. Es muy utilizado en ciencia de datos y aprendizaje automático porque ofrece acceso a potentes recursos de hardware como GPUs.

### b. Ventajas de Google Colab

- Acceso inmediato: Solo necesitas una cuenta de Google para empezar a usarlo.
- Recursos en la nube: Puedes usar GPUs y TPUs para tareas que requieren mucha capacidad de procesamiento.
- Colaboración: Permite compartir notebooks con otras personas de manera similar a Google Docs, facilitando el trabajo en equipo.

### c. Primeros pasos con Google Colab

1. Accede a Google Colab desde [colab.research.google.com](https://colab.research.google.com/).
2. Inicia sesión con tu cuenta de Google.
3. Crea un nuevo notebook seleccionando "Nuevo cuaderno" en la esquina inferior derecha.
4. Para ejecutar código, simplemente escribe en las celdas y presiona "Shift + Enter".

### d. Ejercicio práctico

Vamos a probar el entorno de Google Colab ejecutando un código simple:

1. Abre Google Colab.
2. Crea un nuevo notebook.
3. Escribe y ejecuta el siguiente código en una celda:

```python
print("¡Hola, bienvenidos al curso de Python!")
```
	

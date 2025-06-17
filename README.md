# Curso de Python

### IDE:

* Visual Studio Code: https://code.visualstudio.com/

* Cursor IDE: https://www.cursor.com/en

* PyCharm: https://www.jetbrains.com/es-es/pycharm/download/?section=windows

* Google Colaboratory: https://colab.research.google.com/

### Python

* 3.12.10: https://www.python.org/downloads/release/python-31210/

1. Descargar el exe
2. Ejecutar como administrador
3. Customize installation
4. seleccionar la opción Añadir al PATH.
5. Install Python 3.12 for all users
6. Ruta donde instalarlo: C:\Program Files\Python312

La 3.12 es la más compatible con bibliotecas como por ejemplo TensorFlow, la 3.13 no es compatible con TensorFlow.

Comprobar si está instalado con el siguiente comando en Terminal:

python --version

Si lo hemos instalado pero no hemos seleccionado el PATH se puede volver a ejecutar el instalador, ahí debería volver a preguntar si queremos modificar la instalación existente entonces podemos decir que sí y marcar el PATH.

### Extensiones de VSCode:

* Python (ms-python.python)
* Python Debugger
* Python Environments (ms-python.vscode-python-envs) (Está en prerelease)
    * Esta sustituye a esta: Python Environment Manager (deprecated)
* Pylance
* Jupyter (ms-toolsai.jupyter)
* GitHub Copilot
* vscode-icons (opcional, para cambiar iconos )
* SonarQube for IDE (opcional): extensión para análisis estático de código

### ARCHIVOS 

* .py: son archivos python normal que se pueden ejecutar por consola o con visual studio code o pycharm.

* .ipynb: son archivos jupyter notebook, se puede abrir en diferentes entornos: anaconda, visual studio code, pycharm professional, google colab. En todos se puede ejecutar un notebooks.

En vscode al abrir uno de estos archivos ya nos detecta los intérpretes de Python y nos dejará seleccionar el intérprete que queramos para ejecutar el programa.

### ENTORNO VIRTUAL

* En aplicaciones node es habitual tener: package.json y node_modules con todas las dependencias.
* En Java es habitual: pom.xml o build.gradle con las dependencias y una carpeta target

En Python es habitual tener también un entorno con dependencias.

Esto se logra con:
* pip: gestor de paquetes python. Ejemplo: pip install numpy requests
* requirements.txt

Crear entorno virtual:

* Opción 1: visualmente, pulsamos sobre el intérprete de un archivo python y nos abre una pestaña para Crear nuevo entorno virtual, esto permite crear entorno e instalar de golpe todas las dependencias de requirements.txt

* Opción 2: hacerlo con comandos:
    * Crear entorno virtual:
        * python -m venv .venv
    * Activar entorno virtual:
        * Windows powershell: .venv\Scripts\activate
        * Bash: source .venv/Scripts/activate
    * Instalar una dependencia:
        * pip install requests
    * Instalar todas las dependencias de golpe:
        * pip install -r requirements.txt

pip es un gestor de paquetes.

Repositorio de paquetes: https://pypi.org

Habitual agregar .venv al archivo .gitignore para evitar subir esa carpeta a GitHub ya que son dependencias y puede pesar bastante.

### ESQUEMA SINTAXIS PYTHON:

* Ejecutar vs. Depurar
* Tipos de datos: str, int, float, bool, complex
* Palabras clave (keywords) de lenguaje Python: https://docs.python.org/3/reference/lexical_analysis.html#keywords
* Conversiones de tipos: str(), int(), float()
* Operaciones con textos str: split(), replace(), len()
* Operadores:
    * Aritméticos: *, +, -....
    * Asignación: =
    * Comparación: ==, >=, <=, >, < (Devuelve Boolean True o False)
    * lógicos: and, or, not (Devuelve Boolean True o False)
    * membresía: in, not in (Devuelve Boolean True o False)
    * identidad: is, is not (Devuelve Boolean True o False)
    * bit
* Estructuras de control condicional
    * if, elif, else
    * operador ternario: todo en una misma línea
    * match
* Estructuras de control iterativo (bucles, loops)
    * for: (determinado porque se conocen de antemano cuántas iteraciones puede haber)
        * iterar sobre las letras de un string
        * iterar sobre las palabras de una frase
        * iterar sobre una estructura de datos: lista
    * while (indeterminado)
        * iterar en base a condiciones booleanas, por ejemplo programa interactivo de consola
    * break
    * continue
    * Iteradores avanzados: enumerate, zip
    * Comprehensions: todo en una misma línea
* Estructuras de datos (nativas de Python, sin necesidad de instalar nada):
    * CRUD:
        * Create
        * Retrieve o Read
        * Update
        * Delete (crítico)
    * Listas: []
        * En java: int[] calificaciones = new int[5];
        * En java: ArrayList<Integer> calificaciones = new ArrayList<>();
        * En java: var calificaciones = List.of(1, 2, 3)
        * En python: calificaciones = [1, 2, 3, 4, 5]
        * Características: mutables, ordenadas (asc, desc), permiten duplicados
        * Nomenclatura: se recomienda nombrar las listas en plural: products, users, results
        * Creación:
            * ``[]``
            * ``list(iterable)``
        * Métodos:
            * ``len(nombres)``
            * ``append(x)``: añade un elemento al final
            * ``insert(x)``: insertar en una posición específica
            * ``remove(x)``: eliminar primera ocurrencia
            * ``pop(i)``: eliminar y devolver por índice
            * ``index(x)``: obtener índice de elemento
            * ``count(x)``: contar ocurrencias de un elemento
            * ``sort()``: ordenar inplace (modifica la estructura actual en vez de devolver una nueva)
            * ``reverse()``: invertir orden
            * ``extend(iterable)``: añadir una lista a otra lista
        * Cuándo usar: para colecciones que quieres modificar frecuentemente como por ejemplo carrito de la compra, lista de objetos producto.

    * Tuplas: ()
        * Características: inmutables, ordenadas, permiten duplicados
        * Creación:
            * ``(,)``: Cuidado, porque si no hay coma igual no crea la tupla: 
                * (1) --> Esto no es una tupla
                * (1,) --> Esto sí es una tupla
            * ``tuple(iterable)``
        * Métodos
            * ``count(x)``: contar ocurrencias
            * ``index(x)``: encontrar índice de un elemento
            * Desempaquetar: a, b, c = tupla
        * Cuándo usar: datos de solo lectura, coordenadas (x, y), configuraciones, resultados de una consulta de select de base de datos SQL (una fila de base de datos).
        * En Pandas: df.shape devuelve una tupla con el número de filas y columnas en el dataframe.

    * Diccionarios: {}
        * Características: mutables, ordenado por inserción, claves únicas
        * Creación:
            * ``{ key1 : value1, key2 : value2}``
            * ``dict(iterable)``
        * Ejemplo: ``{"id": 1, "title": "Ordenador ASUS 1551"}``
        * Es una estructura de clave (key) y valor (value)
        * Métodos:
            * ``get("key", default)``: obtener valor y si no lo tiene devuelve el valor por defecto.
            * ``keys()``: obtener todas las claves
            * ``values()``: obtener los valores
            * ``items()``: acceder a los pares de clave y valor
            * ``pop(key)``: borrar por clave y obtener value
            * ``update(dict)``: actualizar con otro diccionario
            * ``setdefault(key, default)``: insertar si no existe
        * Cuándo usar: mapear relaciones clave-valor como por ejemplo contadores, búsqueda por identificador, se usa normalmente para evitar if else largos.

    * Conjuntos: {}
        * Características: elementos únicos (no admiten duplicados), no ordenados 
        * Formas de crearlos: 
            * ``{value1, value2}``
            * `set(iterable)`
        * Métodos:
            * ``add(x)``: añadir elemento
            * ``remove(x)``: eliminar elemento (error si no existe)
            * ``discard(x)``: eliminar elemento (sin error)
            * ``set1.union(set2)`` o ``|`` : unión
            * ``set1.intersection(set2)`` o ``&``: insersección
            * ``set1.difference(set2)`` o ``-``: diferencia. Cuidado porque depende desde qué posición se calcule, ver script de python.
            * ``set1.issubset(set2)``
        * Variante:
            * ``frozenset()``: set inmutable, que podría ser usado como claves de diccionarios.


    * Anidar estructuras de datos:
        * Es común anidar estructuras. Por ejemplo un select a base de datos trae una lista de tuplas.
        * Tener una lista de diccionarios.
        * Tener un diccionario dentro de otro diccionario
    * Otras estructuras: 
        * TypedDict https://peps.python.org/pep-0589/
        * módulo collections
        * biblioteca numpy
        * pandas...
* Funciones
    * Bloques de código reutilizable
    * Evita duplicar código
    * Hace que el código sea más legible al poder proporcionar un nombre a un bloque de código
    * Hace que el código sea más modular, limpio, legible, mantenible, aumenta la usabilidad, evita duplicados.
    * Se crean con:
        * ``def nombre_funcion(x1, x2, ...): ... return ...``
        * ``lambda x: x ** 2 ``
    * Tipos de parámetros:
        * Posicionales: def funcion(a, b)
        * Por defecto: def funcion(a, b=10)
        * Keyword-only: def funcion(a, *, b, c)
        * argumentos variables: def funcion(*numeros)
        * docstring: comentarios para ayudar a entender cómo usar las funciones
        * Arbitrarios por palabra clave: def funcion(**kwargs)

* Módulos:
    * Son archivos .py que se pueden importar en otros archivos .py
    * Se pueden crear módulos propios
    * Se pueden importar módulos de la biblioteca estándar de Python:
        * math
        * datetime
        * random
        * json
        * re
        * Ver todas: https://docs.python.org/3/library/index.html
        * Vienen preinstaladas
    * Sintaxis para importar módulos:
        * from
        * import
        * as
        * Opción 1: Si el módulo python por ejemplo functions.py está en el directorio entonces se puede importar de forma directa: import functions
        * Opción 2: Si el módulo python por ejemplo functions.py está en otro directorio diferente entonces puede requerir usar path para ubicar:
            * import sys
            * sys.path.append("/ruta/completa/directorio')
            * import functions
        * Opción 3: En ese caso es más recomendable construir un paquete e instalarlo


* Paquetes:
    * Son directorios que contienen módulos
    * Se pueden crear paquetes propios
    * Se pueden importar paquetes de la biblioteca estándar de Python
    * Buscar paquetes creados por la comunidad: https://pypi.org/
    * pip install nombre-paquete

* Entrada y salida
    * input()
    * print()

* Gestión de errores:
    * try
    * except
    * finally
    * raise
    * Ejemplos:
        * Cuando se leen datos de la entrada input
        * Cuando se manipulan estructuras de datos u objetos
        * Casos límite, validaciones
        * Acceso a filesystem, carpetas, archivos
        * Comunicaciones por HTTP
        * Acceso a bases de datos
         
* Archivos:
    * with
    * open
    * file.read, file.write
    * encoding='utf-8' para garantizar leer bien acentos y carácteres especiales
    * Windows: 
        * usa barras invertidas (`\`) backslash
        * a veces es necesario escapar: `directorio\\subcarpeta\\archivo.txt`
    * Linux/macOS: usa barras normales (`/`) forward slash
    * opción 1 rawstrings:
        * similar al string formateados fstring existe los raw string rstring:
            * ruta = r'C:\carpeta\subcarpeta\archivo.txt' para evitar problemas de que detecte que `\s` es un caracter de escape
            * ruta = 'C:\\carpeta\\subcarpeta\\archivo.txt'
            * ruta = '/carpeta/subcarpeta/archivo.txt'
    * os
        * os.path.join('directorio','subcarpeta')
    * pathlib (más moderna y recomendable)
        * ruta = Path('directorio') / 'archivo1.txt' # se adapta al SO



* Programación Orientada a Objetos
    * Paradigma de programación presente en muchos lenguajes de programación
    * Representar objetos de la realidad en el lenguaje de programación
    * Clases: ``class``
        * La clases un molde o un plano que define qué atributos y métodos tendrán los objetos.
        * Sería algo similar a la definición de una tabla de base de datos relacional.
        * User, Customer, Product, Category, Technology, Manufacturer, Review, BankAccount
    * Objetos:
        * Instancia concreta de una clase, tendrán los atributos y métodos definidos en la clase, de tal manera que todos los objetos de una clase tendrán esa misma estructura. Aunque cada uno podrá tener valores diferentes en sus atributos.
        * Es una "instancia" de una clase, es algo concreto creado a partir del molde.
        * ``user = User()``
    * Constructor: 
        * Método función especial que se usa para inicializar objetos con valores concretos en sus atributos.
        * Se ejecuta automáticamente al crear un objeto, no hay que invocarlo explícitamente.
        * ``__init__(self, atributo1, atributo2, ...)``
        * `self` se refiere al objeto que estamos creando cuando invocamos la clase: ``User()``
        * Equivalente a `this` en javascript o java.
        * Normalmente se usa para asignar valores a los atributos del objeto que se está creando.
        * También permite hacer comprobaciones, procesar algún valor de entrada, operaciones.
    * Atributos
        * A nivel de clase:
            * Normalmente se usan para valores que no cambian y queremos que sean iguales para todos los objetos.
        * A nivel de instancia (en el constructor):
            * Normalmente serán los atributos que usemos y que permitirán a cada objeto tener valores distintos.

    * Composición y Asociaciones
    * Encapsulación
    * Métodos estáticos a nivel de clase
    * Herencia
    * Tipado:
        * módulo typing
        * módulo enum
        * librería Pydantic
        * Analizador de tipos mypy
    * Polimorfismo


* Base de datos:
    * Opción 1: 
        * Crear base de datos y tablas con SQL directamente en la base de datos, luego con un ORM (sqlalchemy) conectarse a la base de datos y autogenerar el código de las clases Python para cada una de las tablas de base de datos.
    * Opción 2: 
        * Crear clases de Python utilizando herencia con SQLAlchemy ORM, y al ejecutar Python se generan las tablas de SQL automáticamente. 
        * Una vez generadas las tablas, si queremos evolucionar nuestro esquema para agregar nuevas columnas utilizamos un sistema de control de versiones y migraciones como por ejemplo "alembic" https://alembic.sqlalchemy.org/en/latest/autogenerate.html



Ejemplo de clase en JavaScript:

```javascript
class User {
    constructor(email, password) {
        this.email = email;
        this.password = password;
    }
    info() {
        return `Email: ${this.email}` 
    }
}
```

en python

```python
class User:
    def __init__(self, email, password): # dunder methods
        self.email = email
        self.password = password
    #...
```


Paradigmas:

* Estructurada: if, else, match, for, while, def
* Programación Orientada a Objetos: clases, objetos, encapsulación, herencia, composición, polimorfismo, patrones de diseño, principios SOLID
* Programación funcional: código conciso y declarativo: map(), filter(), forEach()
* Programación reactiva: asincronía y programación funcional, RxJS, Signals, Reactor, async, fastapi

Técnicas:
* Catálogo de técnicas de refactorización para crear código limpio y fácil de leer: 
    * https://refactoring.guru/refactoring/techniques/composing-methods


La sintaxis es la base para luego desarrollar cualquier tipo de aplicación:

* Aplicación web: Django, Flask, Streamlit
* Scripts: backups, operación automatizada
* Ciberseguridad
* Ciencia de datos: machine learning y deep learning
* Análisis de datos, Business Intelligence
* IA Generativa

## INTEGRACIÓN CONTINUA

* GitHub Actions
* GitLab CI
* Jenkins
* Travis CI

En el caso de Python:

pip install mypy

mypy hello.py

Ejemplo de error de tipos detectado con mypy:

```txt
C:\dev\curso-2025-05-python\010.oop>mypy product.py
product.py:10: error: Argument 2 to "Product" has incompatible type "str"; expected "float"  [arg-type]
product.py:10: error: Argument 4 to "Product" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

si todo va bien:

```txt
C:\dev\curso-2025-05-python\010.oop>mypy product.py
Success: no issues found in 1 source file
```

## TERMINAL POR DEFECTO:

Ctrl + Shift + P

terminal select default

Esto permite usar cmd como terminal por defecto.

## FRAMEWORKS

* Backend:
    * Se ejecuta en el servidor
    * Opciones:
        * Python
            * Django
                * Django Templates 
            * Flask 
                * Jinja 2
            * FastAPI (Más moderno)
            * Streamlit
                * Más orientado a ciencia de datos y proporciona componentes de python y no es necesario programar html css ni js
        * JavaScript:
            * Nodejs
            * Express
            * Nest
            * Nextjs
        * C#
            * ASP.NET
        * Java
            * Spring Boot

* Frontend: 
    * Se ejecuta en el servidor
    * JavaScript o TypeScript
    * React o Angular o Vue
    * HTML, CSS, Tailwind CSS, Bootstrap CSS, iconos


Recomendación para Desarrollo web Backend-Frontend-FullStack:

* Aprender al menos un framework de backend
* Aprender un poco de frontend: html, css, js, algún framework como React o Angular

## FRAMEWORKS PARA PYTHON

Frameworks para desarrollo web:

* FastAPI
    * Permite crear rápidamente API REST con operaciones CRUD
    * Modelos Pydantic
    * ideal para microservicios
    * Ideal para devolver JSON desde API REST
    * También se puede usar HTML con Jinja
    * Moderna
    * Más liviano

* Django: 
    * Viene con todo incluído
    * Más habituales para aplicaciones full stack

Ciencia de datos:

* Streamlit: 
    * componentes ya hechos
    * más orientado a ciencia de datos y prototipos rápidos

* numpy
* scipy
* pandas
* matplotlib
* seaborn
* plotly
* scikit learn (machine learning y preparación de datos)
* tensorflow (redes neuronales)
* pytorch (redes neuronales)
* transformers

IA Generativa:

* openai
* anthropic
* langchain
* langgraph
* crewai
* ai-sdk (de vercel, javascript)


## BASES DE DATOS EN PYTHON

* MySQL
* MongoDB
* SQLite
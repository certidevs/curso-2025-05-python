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

    * Tuplas: ()
    * Diccionarios: {}
    * Conjuntos: {}
        * Características: elementos únicos
    * Otras estructuras: TypedDict, módulo collections, biblioteca numpy, pandas...
* Funciones
* Entrada y salida
    * input()
    * print()
* Gestión de errores:
    * try
    * except
    * finally


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

## TERMINAL POR DEFECTO:

Ctrl + Shift + P

terminal select default

Esto permite usar cmd como terminal por defecto.

## FRAMEWORKS

* Django
* Flask
* FastAPI
* Streamlit
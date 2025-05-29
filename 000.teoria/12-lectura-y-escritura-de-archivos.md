---
title: 12. Lectura y escritura de archivos
---
> ⚠️ **Atención**:
> Puedes descargar la versión de esta sección en formato notebook [aquí](./resources/12_lectura_de_archivos.ipynb).  
	

# Lectura y escritura de archivos

## 1. Lectura de archivos

En Python, se pueden leer archivos utilizando la función `open()` en combinación con varios modos de apertura. El modo más común es el modo de lectura (`"r"`), que permite abrir un archivo y leer su contenido.

### a. Lectura de un archivo de texto


```python
# Abrir un archivo en modo lectura
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

# Mostrar el contenido del archivo
print(contenido)
```
> Esta es una nueva línea de texto.  
> Se añadirá esta segunda línea.  
    


En este ejemplo, el archivo `archivo.txt` se abre en modo lectura (`"r"`), y su contenido se lee usando `read()`. Utilizamos `with` para asegurarnos de que el archivo se cierre automáticamente al final del bloque.
	
### b. Lectura línea por línea


```python
# Abrir el archivo y leerlo línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina los saltos de línea al final de cada línea
```
> Esta es una nueva línea de texto.  
> Se añadirá esta segunda línea.  
	

Aquí, el archivo se lee línea por línea usando un bucle `for`, lo que resulta útil para manejar archivos grandes.
	

## 2. Escritura en archivos

Para escribir en un archivo, se usa el modo de escritura (`"w"`) o el modo de añadir contenido (`"a"`). El modo `"w"` sobrescribirá el archivo si ya existe, mientras que `"a"` añadirá el nuevo contenido al final del archivo.
	
### a. Creación/Escritura de un archivo de texto

```python
# Escribir en un archivo (sobreescribir si ya existe)
with open("archivo.txt", "w") as archivo:
    archivo.write("Esta es una nueva línea de texto.\n")
    archivo.write("Se añadirá esta segunda línea.\n")
```

Este código crea un archivo `archivo.txt` (o lo sobrescribe si ya existe) y escribe dos líneas de texto.
	

## 3. Lectura y escritura de archivos CSV

Python ofrece soporte nativo para manipular archivos CSV (valores separados por comas) a través del módulo `csv`.

### a. Lectura de un archivo CSV

```python
import csv

# Leer un archivo CSV
with open("datos.csv", newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
```
> `['Nombre', 'Edad', 'Ciudad']`  
> `['Ana', '28', 'Buenos Aires']`  
> `['Carlos', '35', 'Córdoba']`  
	

Este ejemplo muestra cómo leer un archivo CSV y mostrar cada fila como una lista.
	
### b. Escritura en un archivo CSV

```python
import csv

# Escribir en un archivo CSV
with open("datos.csv", "w", newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Nombre", "Edad", "Ciudad"])
    escritor.writerow(["Ana", 28, "Buenos Aires"])
    escritor.writerow(["Carlos", 35, "Córdoba"])
```

Aquí, se escribe un archivo CSV llamado `salida.csv` con tres columnas (`Nombre`, `Edad`, `Ciudad`) y dos filas de datos.
	

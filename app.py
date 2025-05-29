
menu = """
Welcome to app, select and option:
1 - option1
2 - option2
3 - option3
4 - option4
"""
print(menu)

option = int(input("introduce una opción"))

if option == 1:
    pass
elif option == 2:
    pass
elif option == 3:
    pass
elif option == 4:
    pass
else:
    print('no has seleccionado una opción correcta')

# El programa termina tras la primera interacción

# En una aplicación de consola si queremos el programa continúe en marcha 
# necesitamos estructuras iterativas

# En una aplicación web (flask, fastapi, django) es el framework quien controla la ejecución
# del programa y lo mantiene en marcha
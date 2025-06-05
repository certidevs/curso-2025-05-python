
# Se usa finally para cerrar recursos: ficheros abiertos, bases de datos, conexiones, etc

try:
    print("try1")
    result = 4 / 0
    print("try2")
except:
    print("except")
finally:
    print("finally")
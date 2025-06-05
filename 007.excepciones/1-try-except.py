
# try - except
try:
    print(hola)
except:
    print("Error")

print("Esto está bien")


# try except - múltiple
try:
    num1 = int(input("Introduce un numero:"))
    num2 = int(input("Introduce otro numero:"))
    lista = [1, 2, 3, 4]
    print(lista[676])
    result = num1 / num2
except ValueError:
    print("ValueError1: formato de número incorrecto.")
except ZeroDivisionError:
    print("ZeroDivisionError: error en división.")
except IndexError:
    print("IndexError: acceso fuera del límite de la lista")


print("fin")
"""
Principio Todos somos adultos
Las variables protegidas se pueden acceder desde fuera
"""

class Father:
    _car = "Father's car"  # Variable protegida
    __motorcycle = "Harley"  # Variable encapsulada

    def greeting1(self):
        print("Hola desde Father!")

    def get_car(self):
        print(self._car)


class Child(Father):
    pass


father = Father()
print(father._car)  # La variable está protegida y no debería ser accedida ni modificada desde fuera de la clase
father._car = "Honda"
print(father._car)

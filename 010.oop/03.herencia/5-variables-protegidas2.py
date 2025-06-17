class Father:
    _car = "Father's car"  # variable protegida

    def greeting1(self):
        print("Hola desde Father!")

    def get_car(self):
        print(self._car)

    @property
    def car(self):
        return self._car


class Child(Father):
    pass


father = Father()
print(father.car)  # La variable está protegida y no debería ser accedida ni modificada desde fuera de la clase
father._car = "Honda"
print(father._car)  # Se sigue pudiendo acceder a la variable protegida

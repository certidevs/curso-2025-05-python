"""
Herencia y encapsulación
"""

class Father:
    __car = "Father's car"

    def greeting1(self):
        print("Hola desde Father!")

    def get_car(self):
        print(self.__car)


class Mother:
    __car = "Mother's car"

    def greeting2(self):
        print("Hola desde Mother!")

    def get_car(self):
        print(self.__car)


class Child(Mother, Father):
    pass


child = Child()
child.get_car()
class Father:
    car = "Coche 1"

    def greeting(self):
        print("Hola desde Father!")


class Mother:
    car = "Coche 2"

    def greeting(self):
        print("Hola desde Mother!")


class Child(Mother, Father):
    car = "Coche 3"  # Sobreescribe la propiedad heredada

    def greeting3(self):
        super().greeting()


child = Child()
child.greeting3()

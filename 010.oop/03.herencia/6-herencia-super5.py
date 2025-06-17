class Father:
    car = "Coche 1"

    def greeting1(self):
        print("Hola desde Father!")


class Mother:
    car = "Coche 2"

    def greeting2(self):
        print("Hola desde Mother!")


class Child(Father, Mother):
    car = "Coche 3"  # Sobreescribe la propiedad heredada

    def greeting3(self):
        self.greeting1()
        super().greeting2()


child = Child()
child.greeting3()

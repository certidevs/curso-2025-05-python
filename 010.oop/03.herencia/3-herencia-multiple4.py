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
        print("Hello from child!")


child = Child()
print(child.car)
child.greeting1()
child.greeting2()
child.greeting3()

# Crear objetos de las clases base o superclases
print("==========")
father = Father()
father.greeting1()
mother = Mother()
mother.greeting2()


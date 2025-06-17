class Father:
    car = "Coche 1"


class Mother:
    car = "Coche 2"


class Child(Father, Mother):
    car = "Coche 3"  # Sobreescribe la propiedad heredada


child = Child()
print(child.car)



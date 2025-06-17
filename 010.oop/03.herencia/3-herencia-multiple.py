class Father:
    car = "Coche 1"


class Mother:
    car = "Coche 2"


class Child(Mother, Father):  # Por defecto tiene prioridad el primero del que se hereda
    pass


child = Child()
print(child.car)



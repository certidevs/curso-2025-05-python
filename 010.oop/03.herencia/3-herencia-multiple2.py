class Father:
    car1 = "Coche 1"


class Mother:
    car2 = "Coche 2"


class Child(Father, Mother):
    pass


child = Child()
print(child.car1)
print(child.car2)



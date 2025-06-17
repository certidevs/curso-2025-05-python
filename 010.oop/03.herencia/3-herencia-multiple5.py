"""
Múltiples niveles de 2.herencia
"""

class GrandMother1:
    pass

class GrandFather1:
    pass

class Mother(GrandMother1, GrandFather1):
    pass


class GrandMother2:
    pass

class GrandFather2:
    pass

class Father(GrandMother2, GrandFather2):
    pass

class Child(Mother, Father):
    pass
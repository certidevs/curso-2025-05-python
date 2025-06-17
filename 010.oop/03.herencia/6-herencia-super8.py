class Father:
    def __init__(self, name):
        print("Constructor Father")
        self.name = name


class Mother:
    def __init__(self, lastname):
        print("Constructor Mother")
        self.lastname = lastname


class Child(Mother, Father):
    def __init__(self, name, lastname):
        Father.__init__(self, name)  # Otra forma de invocar el constructor de las clases base
        Mother.__init__(self, lastname)


child = Child("Alan", "Sastre")
print(child.name)
print(child.lastname)
print("fin")

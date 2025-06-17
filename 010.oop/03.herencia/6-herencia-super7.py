class Father:
    def __init__(self, name):
        print("Constructor Father")
        self.name = name


class Mother:
    def __init__(self, name):
        print("Constructor Mother")
        self.name = name


class Child(Mother, Father):
    def __init__(self, name, lastname):
        super().__init__(name)
        self.lastname = lastname


child = Child("Alan", "Sastre")
print("fin")

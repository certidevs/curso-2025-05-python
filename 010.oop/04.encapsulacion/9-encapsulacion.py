
class Account:
    def __init__(self, titular, balance, color):
        self.titular = titular
        self.balance = balance
        self.__color = color  # encapsulado

    def get_color(self):
        return self.__color  # Al estar dentro de la clase SÍ tenemos acceso a atributos encapsulados

    def set_color(self, color):
        if color == "red" and self.balance < 0:
            self.__color = color

    def __str__(self):
        return f"Account(titular={self.titular}, " \
               f"balance={self.balance}, " \
               f"color={self.__color} " \
               f")"

    def __repr__(self):
        return self.__str__()


savings_account = Account("ALAN SMITH", -200, "red")
holidays_account = Account("ALAN SMITH", 3000, "green")

# print(savings_account.__color)  # No es accesible porque está encapsulado
# Para cambiarlo es necesario utilizar el método set_color

# métodos getter y setter
savings_account.set_color("green")  # set_color para cambiar el color
print(savings_account)

print(savings_account.get_color())  # get_color para obtener el color

savings_account.performance = 4
print(savings_account.performance)

savings_account.__color = "orange"

print(savings_account.__color)
print(savings_account.get_color())
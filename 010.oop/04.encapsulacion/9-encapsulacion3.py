
class Account:
    def __init__(self, titular, balance, color):
        self.titular = titular
        self.__balance = balance  # encapsulado
        self.__color = color  # encapsulado

    # getter para acceder a los atributos encapsulados
    def get_color(self):
        return self.__color  # Al estar dentro de la clase SÍ tenemos acceso a atributos encapsulados

    def get_balance(self):
        return self.__balance

    # setter para cambiar atributos encapsulados
    def set_balance(self, balance):
        self.__adjust_color(balance)
        # assing new balance
        self.__balance = balance

    # método interno pensado para ser invocado desde otros métodos de la clase, pero no desde fuera
    def __adjust_color(self, balance):
        # check color
        if balance < 0:
            self.__color = "red"
        elif balance == 0:
            self.__color = "blue"
        else:
            self.__color = "green"

    def add_ingresos(self, ingresos):
        for ingreso in ingresos:
            self.set_balance(self.__balance + ingreso)

    def sub_expenses(self, expenses):
        for expense in expenses:
            self.set_balance(self.__balance - expense)

    def __str__(self):
        return f"Account(titular={self.titular}, " \
               f"balance={self.__balance}, " \
               f"color={self.__color} " \
               f")"

    def __repr__(self):
        return self.__str__()


savings_account = Account("ALAN SMITH", -200, "red")

# El método está encapsulado por tanto no es accesible
# savings_account.adjust_color()
# savings_account.__adjust_color()

incomes = [1000, 3000, 1000]
gastos = [200, 100, 50]
savings_account.add_ingresos(incomes)
savings_account.sub_expenses(gastos)
print("fin")
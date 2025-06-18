
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

        # check color
        if balance < 0:
            self.__color = "red"
        elif balance == 0:
            self.__color = "blue"
        else:
            self.__color = "green"

        # assing new balance
        self.__balance = balance

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
savings_account.__balance = -500 # esto en realidad crea otro atributo, no modifica el balance
savings_account.balance = -400 # esto en realidad crea otro atributo, no modifica el balance
print(savings_account.__balance) # esto en realidad accede a otro atributo no al balance real
print(savings_account.balance) # esto en realidad accede a otro atributo no al balance real

print(savings_account.get_balance()) # esto SÍ accede al balance real


# check balance and color
print(savings_account)
savings_account.set_balance(200)
print(savings_account)
savings_account.set_balance(0)
print(savings_account)

# check incomes
print("Balance actual:", savings_account.get_balance(), savings_account.get_color())
incomes = [1000, 1500, 2100]
savings_account.add_ingresos(incomes)
print("Balance después de ingresos:", savings_account.get_balance(), savings_account.get_color())

# check expenses
expenses = [400, 5000, 200, 100]
savings_account.sub_expenses(expenses)
print("Balance después de gastos:", savings_account.get_balance(), savings_account.get_color())

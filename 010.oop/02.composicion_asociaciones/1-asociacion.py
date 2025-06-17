"""
Asociación: grado de relación más débil
"""


class JobRole:
    def __init__(self, name, umbral):
        self.name = name
        self.umbral = umbral


class Salary:
    def __init__(self, antiguedad):
        self.neto = 0
        self.bruto = 0
        self.antiguedad = antiguedad

    def calculate_salary(self, umbral):
        if self.antiguedad > 10:
            self.bruto = umbral * 2
            self.neto = umbral * 2
        else:
            self.bruto = umbral
            self.neto = umbral


# Creación de objetos
junior_role = JobRole("Junior", 24000)
junior_salary = Salary(1)

# Asociación de objetos
junior_salary.calculate_salary(junior_role.umbral)
del junior_salary  # Si borramos este objeto el otro sigue existiendo
print("fin")
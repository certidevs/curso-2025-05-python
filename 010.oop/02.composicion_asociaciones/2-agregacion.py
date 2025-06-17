"""
Agregación: grado de relación medio
"""


class JobRole:
    def __init__(self, name, umbral):
        self.name = name
        self.umbral = umbral


class Salary:
    def __init__(self, antiguedad, job_role):
        self.neto = 0
        self.bruto = 0
        self.antiguedad = antiguedad
        self.job_role = job_role

    def calculate_salary(self):
        if self.antiguedad > 10:
            self.bruto = self.job_role.umbral * 2
            self.neto = self.job_role.umbral * 2
        else:
            self.bruto = self.job_role.umbral
            self.neto = self.job_role.umbral


# Creación de objetos
junior_role = JobRole("Junior", 24000)
junior_salary = Salary(1, junior_role)  # Agregación


junior_salary.calculate_salary()
del junior_salary  # Si borramos este objeto el otro sigue existiendo
print("fin")

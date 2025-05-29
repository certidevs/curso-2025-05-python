"""
Una tupla no se puede modificar
"""
nominados_tuple1 = ("Alan", "Alba", "Zacarias", "Aroa", "Dani", "Evaristo", "Mario", "Leticia", "Alan", "Alan")
# nominados_tuple1[0] = "Batman"  # Tuples don't support item assignment

nominados_list = list(nominados_tuple1)

nominados_list[0] = "Batman"

nominados_tuple2 = tuple(nominados_list)

print(nominados_tuple2)

if "Alan" in nominados_tuple1:
    print("Verdadero")
else:
    print("Falso")

print("Alan" in nominados_tuple2)
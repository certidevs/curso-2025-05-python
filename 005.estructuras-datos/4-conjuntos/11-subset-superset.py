
# El prefijo is o has denota que el valor de retorno es un boolean

# issubset(): es un subconjunto ?


# False porque names2 no contiene los elementos de names1
names1 = {"Leticia", "Ariel", "Antoni"}
names2 = {"Alan", "Emilio", "Alexánder", "Dani", "Aroa"}
print("names1.issubset(names2):", names1.issubset(names2))
print("===========================")

# True porque names4 SI contiene los elementos de names3
names3 = {"Leticia", "Ariel", "Antoni"}
names4 = {"Alan", "Emilio", "Alexánder", "Dani", "Aroa", "Leticia", "Ariel", "Antoni"}
print("names1.issubset(names2):", names3.issubset(names4))
print("===========================")


# issuperset() - es un superconjunto

names5 = {"Leticia", "Ariel", "Antoni"}
names6 = {"Alan", "Emilio", "Alexánder", "Dani", "Aroa", "Leticia", "Ariel", "Antoni"}
# True porque names6 sí contiene los elementos de names5
print("names6.issuperset(names5):", names6.issuperset(names5))
# False porque names5 no contiene todos los elementos de names6
print("names5.issuperset(names6):", names5.issuperset(names6))
print("===========================")


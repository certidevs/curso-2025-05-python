
# symmetric_difference() - crea nuevo conjunto con elementos no comunes a ambos

names1 = {"name1", "name2", "name3"}
names2 = {"name3", "name4", "name6"}
names3 = names1.symmetric_difference(names2)  # Crea un nuevo conjunto sin name3 porque es común a ambos
print(names3)
print("=========================")
# symmetric_difference_update()
print(names1)
names1.symmetric_difference_update(names2)
print(names1)


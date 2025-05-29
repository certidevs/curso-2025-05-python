
smartphones1 = {"OnePlus", "Apple", "Huawei"}
smartphones2 = {"Xiaomi", "Realme", "Oppo"}

# union()
smartphones3 = smartphones1.union(smartphones2)  # Devuelve un nuevo conjunto
print(smartphones1)
print(smartphones2)
print(smartphones3)
print("==================================")


# update()

smartphones1.update(smartphones2)  # Se actualiza el conjunto que ya existía
print(smartphones1)
print(smartphones2)


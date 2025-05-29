
smartphones1 = {"OnePlus", "Apple", "Huawei"}
smartphones2 = {"OnePlus", "Realme", "Oppo"}

# difference()  - devuelve un nuevo conjunto
difference1 = smartphones1.difference(smartphones2)
difference2 = smartphones2.difference(smartphones1)
print(difference1)
print(difference2)
print("====================")

# difference_update() -- actualiza el primer conjunto

smartphones1.difference_update(smartphones2)
print(smartphones1)
print(smartphones2)




smartphones1 = {"OnePlus", "Apple", "Huawei"}
smartphones2 = {"OnePlus", "Realme", "Oppo"}

# intersection()

smartphones3 = smartphones1.intersection(smartphones2)
print("smartphones1:", smartphones1)
print("smartphones2:", smartphones2)
print("smartphones3:", smartphones3)
print("=================================")

# intersection_update()

smartphones1.intersection_update(smartphones2)
print("smartphones1:", smartphones1)
print("smartphones2:", smartphones2)


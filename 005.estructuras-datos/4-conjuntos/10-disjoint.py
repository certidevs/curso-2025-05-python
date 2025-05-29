
# False porque tienen al menos un elemento en común:
smartphones1 = {"OnePlus", "Apple", "Huawei"}
smartphones2 = {"OnePlus", "Realme", "Oppo"}
print(smartphones1.isdisjoint(smartphones2))


# True porque no tienen ningún elemento en común:
smartphones3 = {"brand1", "brand2"}
smartphones4 = {"brand3", "brand4"}
print(smartphones3.isdisjoint(smartphones4))




# smartphones1 = set("Samsung", "Apple")  # TypeError: set expected at most 1 argument, got 2

smartphones1 = set(("Samsung", "Apple"))  # Tupla

print(smartphones1)
print("===============")

smartphones2 = set(["Samsung", "Apple"])  # Lista

print(smartphones2)
print("===============")

smartphones3 = set({"Samsung", "Apple"})  # Conjunto (set)

print(smartphones3)
print("===============")

smartphones4 = set({"Samsung":"Galaxy", "Apple": "iPhone"})  # Diccionario

print(smartphones4)
print("===============")
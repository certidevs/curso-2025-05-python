
text = "tesla"

for char in text:
    print(char)

print("bye")

names = ["Dani", "Leti", "Alan", "Pablo"]

for name in names:
    print(name)
    check = True

    if name == "Alan":
        continue

    if name == "Leti":
        break

    for char in name: # bucle anidado
        print(char)
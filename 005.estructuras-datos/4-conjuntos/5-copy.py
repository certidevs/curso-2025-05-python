
laptops = {"asus", "dell", "hp", "msi", "lenovo", "ibm"}

# No copia!
laptops2 = laptops

laptops.add("corsair")

print(laptops)
print(laptops2)

# copy()

laptops3 = laptops.copy()

laptops.add("apple")

print(laptops)
print(laptops3)
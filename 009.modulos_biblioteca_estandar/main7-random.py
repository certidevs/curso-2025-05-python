import random

# randrange tiene 3 parámetros

# 1 parámetro
print(random.randrange(9))

# 2 parámetros
print(random.randrange(50, 100))

# 3 parámetros
print(random.randrange(50, 100, 5))

# choice
names = ["Alan", "Leticia", "Evaristo", "Ariel", "Antoni"]
print(random.choice(names))

# random
print(round(random.random() * 100, 2))

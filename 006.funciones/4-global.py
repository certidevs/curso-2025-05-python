number = 10


def saludo():
    global number
    number = 3
    print(number)


saludo()
print(number)

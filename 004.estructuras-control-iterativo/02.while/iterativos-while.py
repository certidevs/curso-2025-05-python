
check1 = 50 < 100
check2 = 100 > 400
check3 = 500 < 1000

cont = 0
while check1 and check2 or check3:
    print("while")
    check1 = True
    check2 = True
    check3 = True
    cont += 1
    if cont == 3:  # Si el contador llega a 3 cambiamos la condicion para salir del bucle
        # check1 = False
        # check3 = False
        break
else:
    print("else")
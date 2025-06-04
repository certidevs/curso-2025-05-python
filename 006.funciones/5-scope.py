def saludo():
    mensaje = "Hola!"
    print(mensaje)


saludo()

# Da error porque la variable mensaje está en el scope de la función y no fuera.
# print(mensaje)
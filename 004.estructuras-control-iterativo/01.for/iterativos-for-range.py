"""
    JavaScript:
    for(let i = 0; i < 10; i++){
        console.log(i)
    }
"""
# comentar bloques Ctrl + ç

# range con un parámetro: fin (excluido)
for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(i)

# range con dos parámetros: inicio (incluido) y fin (excluido)
for i in range(0, 10):
    print(i)

# range con tres parámetros: inicio, fin y step
for i in range(0, 10, 2):
    print(i)

# Ejemplo real:
# para buscar un nickname que no esté ocupado
# alan@gmail.com
# alan
# alan1
# alan2
# alan3
# hasta que esté libre
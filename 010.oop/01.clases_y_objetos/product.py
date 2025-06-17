class Product:
    def __init__(self, name: str, price: float, description: str, size: str, color: str):
        self.name = name
        self.price = price
        self.description = description
        self.size = size    
        self.color = color


camiseta1 = Product("prueba", 34, "Camiseta de poliéster", "L", "Azul")
print(camiseta1.price)
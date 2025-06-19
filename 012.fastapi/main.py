from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

# fastapi dev main.py

@app.get("/") # Mapea peticiones HTTP GET http://localhost:8000/
def hola():
    return {"message": "Hola mundo"}

@app.get("/products/{product_id}") # Mapea peticiones HTTP GET http://localhost:8000/
def find_product(product_id: int):
    # Lo normal sería traer este objeto de base de datos con SQLAlchemy o mysql connector o pymysql
    return Product(id=product_id, name='producto ficticio', price=49.99)
    # return {
    #     "id": product_id,
    #     "name": "producto ficticio"
    # }

@app.post("/products")
def create_product(product: Product):
    print(product)
    product.name = 'Nombre cambiado'
    return product

# @app.put editar
# @app.patch editar parcialmente
# @app.delete borrar

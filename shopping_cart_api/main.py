from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import cart 


app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float

products = [
    Product(id=1, name="Laptop", price=999.99),
    Product(id=2, name="Mouse", price=25.50),
    Product(id=3, name="Keyboard", price=45.75)
]

@app.get("/products/", response_model=List[Product])
def get_products():
    return products

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


@app.post("/cart/add")
def add_to_cart(product_id: int, qty: int):
    try:
        # Find product
        selected_product = None
        for product in products:
            if product.id == product_id:
                selected_product = product
                break

        if not selected_product:
            return {"error": "Product not found"}

        # Load existing cart
        current_cart = cart.load_cart()

        # Add or update item in cart
        found = False
        for item in current_cart:
            if item["product_id"] == product_id:
                item["qty"] += qty
                found = True
                break

        if not found:
            current_cart.append({
                "product_id": product_id,
                "name": selected_product.name,
                "price": selected_product.price,
                "qty": qty
            })

        cart.save_cart(current_cart)
        return {"message": "Product added to cart", "cart": current_cart}

    except Exception as e:
        return {"error": str(e)}


@app.get("/cart/checkout")
def checkout():
    try:
        current_cart = cart.load_cart()
        if not current_cart:
            return {"message": "Cart is empty"}

        total = cart.calculate_total(current_cart)

        return {
            "cart": current_cart,
            "total": total
        }

    except Exception as e:
        return {"error": str(e)}

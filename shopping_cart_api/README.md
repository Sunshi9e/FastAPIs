#  Mini Shopping API with Cart (FastAPI) 🛒

A beginner-friendly FastAPI project to simulate a simple shopping experience. Users can browse products, add them to a cart, and view their checkout total — all using Python basics.

## Features

- View list of available products
- Add items to cart using query parameters
- Compute and round total price during checkout
- Prevents duplicate entries in cart (adds quantity instead)
- Cart data saved to `cart.json` file
- Basic error handling using `try-except`

## Requirements 📦 

- Python 3.7+
- FastAPI
- Uvicorn

## Project Structure 📁 
```
shopping_api/
├── main.py # Main FastAPI app
├── cart.py # Cart logic module
├── cart.json # Auto-created to store cart data
```


## 🛠️ Installation & Running

1. **Clone or create the folder and files:**

2. **Install dependencies:**
    ```
    pip install fastapi uvicorn
    ```
3. **Run the app**
    ```
    uvicorn main:app --reload
    ```

## API Endpoints 📚

1.  **GET /products/** 🛍️
    - Returns a list of available products.

2.  **POST /cart/add?product_id=1&qty=2** ➕
    - Adds a product to the cart. If product already exists, it increases the quantity.
    - Example Request:
    ```
    POST http://127.0.0.1:8000/cart/add?product_id=2&qty=3
    ```
3. **GET /cart/checkout** 💳 
    - Returns the current cart and total amount.- 
    - Response Example:
    ```
    {
        "cart": [
            {
            "product_id": 2,
            "name": "Mouse",
            "price": 25.5,
            "qty": 3
            }
        ],
        "total": 76.5
    }
    ```
## 📘 Notes

- Prices are rounded using Python’s math module (rounded down to 2 decimal places).

- Cart data is stored in a local JSON file (cart.json) automatically.


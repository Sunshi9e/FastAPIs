import json
import os

def load_cart():
    try:
        if os.path.exists("cart.json"):
            with open("cart.json", "r") as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print("Error loading cart:", e)
        return []

def save_cart(cart):
    try:
        with open("cart.json", "w") as f:
            json.dump(cart, f, indent=2)
    except Exception as e:
        print("Error saving cart:", e)

import json, os,  math 

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


def calculate_total(cart_items):
    total = 0
    for item in cart_items:
        total += item["price"] * item["qty"]
    return math.floor(total * 100) / 100 
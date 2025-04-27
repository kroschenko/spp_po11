import requests

class Cart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def total(self):
        total = sum(item["price"] for item in self.items)
        return total * (1 - self.discount / 100)

    def apply_discount(self, discount):
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = discount

    def log_purchase(self, item):
        requests.post("https://example.com/log", json=item)

coupons = {"SAVE10": 10, "HALF": 50}

def apply_coupon(cart, coupon_code):
    if coupon_code in coupons:
        cart.apply_discount(coupons[coupon_code])
    else:
        raise ValueError("Invalid coupon")

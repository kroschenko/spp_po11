class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(item["price"] for item in self.items)

    def apply_discount(self, discount_percent):
        if not (0 <= discount_percent <= 100):
            raise ValueError("Invalid discount percent")
        for item in self.items:
            item["price"] *= (1 - discount_percent / 100)

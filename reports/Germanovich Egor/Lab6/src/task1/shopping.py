import requests


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(item["price"] for item in self.items)

    def apply_discount(self, discount_percent):
        if not 0 <= discount_percent <= 100:
            raise ValueError("Invalid discount percent")
        for item in self.items:
            item["price"] *= 1 - discount_percent / 100

    def log_purchase(self, item):
        requests.post("https://example.com/log", json=item)

    def apply_coupon(self, coupon_code):
        coupons = {"SAVE10": 10, "HALF": 50}
        if coupon_code in coupons:
            self.apply_discount(coupons[coupon_code])
        else:
            raise ValueError("Invalid coupon")

    def remove_item(self, item_name: str) -> None:
        """Удаляет товар из корзины по имени"""
        if not item_name:
            raise ValueError("Имя товара не может быть пустым")
        if item_name not in self.items:
            raise ValueError(f"Товар {item_name} не найден в корзине")
        del self.items[item_name]

import requests

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.items.append({"name": name, "price": price})

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def apply_discount(self, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100 percent")
        for item in self.items:
            item["price"] *= (1 - discount_percent / 100)

    def log_purchase(self, item):
        response = requests.post("https://example.com/purchase", json=item)
        if response.status_code == 200:
            print("Покупка успешно зарегистрирована!")
        else:
            print("Ошибка при регистрации покупки!")

    def apply_coupon(self, coupon_code):
        coupons = {"DISCOUNT20": 20, "HALFOFF": 50}
        if coupon_code in coupons:
            self.apply_discount(coupons[coupon_code])
        else:
            raise ValueError("Неверный код купона")

    def remove_item(self, name):
        if not name:
            raise ValueError("Item name cannot be empty")
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"Товар '{name}' удалён из корзины")
                return
        raise ValueError(f"Товар '{name}' не найден в корзине")

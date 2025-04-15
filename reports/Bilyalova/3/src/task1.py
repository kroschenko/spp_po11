class Burger:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

class VeganBurger(Burger):
    def __init__(self):
        super().__init__("Веганский бургер", 5.0)

class ChickenBurger(Burger):
    def __init__(self):
        super().__init__("Куриный бургер", 6.0)

class Drink:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"


class ColdDrink(Drink):
    def __init__(self):
        super().__init__("Холодный напиток (Пепси)", 2.0)

class HotDrink(Drink):
    def __init__(self):
        super().__init__("Горячий напиток (Кофе)", 3.0)

class Packaging:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

class TakeawayPackaging(Packaging):
    def __init__(self):
        super().__init__("Упаковка с собой", 0.5)

class OnSitePackaging(Packaging):
    def __init__(self):
        super().__init__("Упаковка на месте", 0.0)

class Order:
    def __init__(self):
        self.burger = None
        self.drink = None
        self.packaging = None

    def set_burger(self, burger: Burger):
        self.burger = burger

    def set_drink(self, drink: Drink):
        self.drink = drink

    def set_packaging(self, packaging: Packaging):
        self.packaging = packaging

    def calculate_total(self) -> float:
        total = 0
        if self.burger:
            total += self.burger.price
        if self.drink:
            total += self.drink.price
        if self.packaging:
            total += self.packaging.price
        return total

    def __str__(self):
        return (f"Заказ:\n"
                f"  Бургер: {self.burger}\n"
                f"  Напиток: {self.drink}\n"
                f"  Упаковка: {self.packaging}\n"
                f"Итого: ${self.calculate_total()}")

class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_burger(self, burger: Burger):
        self.order.set_burger(burger)
        return self

    def add_drink(self, drink: Drink):
        self.order.set_drink(drink)
        return self

    def add_packaging(self, packaging: Packaging):
        self.order.set_packaging(packaging)
        return self

    def build(self) -> Order:
        return self.order

if __name__ == "__main__":
    # Создаем строителя
    builder = OrderBuilder()

    # Формируем заказ
    order1 = (builder
              .add_burger(VeganBurger())
              .add_drink(ColdDrink())
              .add_packaging(TakeawayPackaging())
              .build())

    order2 = (builder
              .add_burger(ChickenBurger())
              .add_drink(HotDrink())
              .add_packaging(OnSitePackaging())
              .build())

    # Выводим информацию о заказах
    print("Заказ 1:")
    print(order1)

    print("\nЗаказ 2:")
    print(order2)

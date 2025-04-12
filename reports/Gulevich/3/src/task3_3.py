from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict


class PizzaType(Enum):
    MARGHERITA = "Маргарита"
    PEPPERONI = "Пепперони"
    BBQ = "Барбекю"
    SEAFOOD = "Морепродукты"
    VEGETARIAN = "Вегетарианская"


class PizzaSize(Enum):
    SMALL = "Маленькая"
    MEDIUM = "Средняя"
    LARGE = "Большая"


@dataclass
class Pizza:
    type: PizzaType
    size: PizzaSize
    price: float


@dataclass
class Order:
    order_id: int
    pizzas: List[Pizza] = field(default_factory=list)
    is_cancelled: bool = False

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def cancel(self):
        self.is_cancelled = True

    def get_total(self) -> float:
        return sum(pizza.price for pizza in self.pizzas)

    def __str__(self):
        status = "Отменен" if self.is_cancelled else "Активен"
        pizzas = "\n".join(f"  - {pizza.size.value} {pizza.type.value}: ${pizza.price:.2f}"
                           for pizza in self.pizzas)
        return (f"Заказ #{self.order_id} ({status})\n"
                f"{pizzas}\n"
                f"Итого: ${self.get_total():.2f}")


class Pizzeria:
    def __init__(self):
        self.orders: Dict[int, Order] = {}
        self.next_order_id = 1
        self.price_list = {
            PizzaSize.SMALL: 8.99,
            PizzaSize.MEDIUM: 12.99,
            PizzaSize.LARGE: 16.99
        }

    def create_order(self) -> Order:
        order = Order(self.next_order_id)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order

    def get_order(self, order_id: int) -> Order:
        return self.orders.get(order_id)

    def cancel_order(self, order_id: int) -> bool:
        order = self.get_order(order_id)
        if order and not order.is_cancelled:
            order.cancel()
            return True
        return False

    def reorder(self, order_id: int) -> Order:
        original = self.get_order(order_id)
        if not original:
            return None

        new_order = self.create_order()
        for pizza in original.pizzas:
            new_order.add_pizza(Pizza(pizza.type, pizza.size, pizza.price))
        return new_order

    def show_menu(self):
        print("\nМеню пиццерии:")
        print("Размеры:")
        for size in PizzaSize:
            print(f"  {size.value}: ${self.price_list[size]:.2f}")
        print("\nВиды пицц:")
        for pizza_type in PizzaType:
            print(f"  {pizza_type.value}")

    def create_pizza(self) -> Pizza:
        print("\nВыберите вид пиццы:")
        for i, pizza_type in enumerate(PizzaType, 1):
            print(f"{i}. {pizza_type.value}")

        type_choice = int(input("Ваш выбор (1-5): ")) - 1
        pizza_type = list(PizzaType)[type_choice]

        print("\nВыберите размер:")
        for i, size in enumerate(PizzaSize, 1):
            print(f"{i}. {size.value}")

        size_choice = int(input("Ваш выбор (1-3): ")) - 1
        pizza_size = list(PizzaSize)[size_choice]

        price = self.price_list[pizza_size]
        return Pizza(pizza_type, pizza_size, price)


def handle_order_creation(pizzeria):
    order = pizzeria.create_order()
    pizzeria.show_menu()

    while True:
        pizza = pizzeria.create_pizza()
        order.add_pizza(pizza)
        print(f"\nПицца добавлена в заказ #{order.order_id}")

        more = input("Добавить еще пиццу? (да/нет): ").lower()
        if more != "да":
            break

    print(f"\nЗаказ #{order.order_id} создан:")
    print(order)
    return order


def show_active_orders(pizzeria):
    print("\nАктивные заказы:")
    for order in pizzeria.orders.values():
        if not order.is_cancelled:
            print(order)
            print("-" * 30)


def handle_order_cancellation(pizzeria):
    order_id = int(input("Введите номер заказа для отмены: "))
    if pizzeria.cancel_order(order_id):
        print(f"Заказ #{order_id} отменен")
    else:
        print("Не удалось отменить заказ (не найден или уже отменен)")


def handle_reorder(pizzeria):
    order_id = int(input("Введите номер заказа для повторения: "))
    new_order = pizzeria.reorder(order_id)
    if new_order:
        print(f"\nНовый заказ #{new_order.order_id} создан (копия #{order_id}):")
        print(new_order)
    else:
        print("Заказ не найден")


def main():
    pizzeria = Pizzeria()

    while True:
        print("\nГлавное меню:")
        print("1. Создать новый заказ")
        print("2. Просмотреть активные заказы")
        print("3. Отменить заказ")
        print("4. Повторить заказ")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            handle_order_creation(pizzeria)
        elif choice == "2":
            show_active_orders(pizzeria)
        elif choice == "3":
            handle_order_cancellation(pizzeria)
        elif choice == "4":
            handle_reorder(pizzeria)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()


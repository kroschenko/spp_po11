from abc import ABC, abstractmethod

# Абстрактный класс для напитков
class Coffee(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Конкретные классы напитков
class Espresso(Coffee):
    def get_name(self):
        return "Эспрессо"

    def get_ingredients(self):
        return ["кофе", "вода"]

    def get_cost(self):
        return 2.5


class Americano(Coffee):
    def get_name(self):
        return "Американо"

    def get_ingredients(self):
        return ["кофе", "вода", "горячая вода"]

    def get_cost(self):
        return 3.0


class Cappuccino(Coffee):
    def get_name(self):
        return "Капучино"

    def get_ingredients(self):
        return ["кофе", "вода", "молоко", "пена"]

    def get_cost(self):
        return 4.0


class Latte(Coffee):
    def get_name(self):
        return "Латте"

    def get_ingredients(self):
        return ["кофе", "вода", "молоко"]

    def get_cost(self):
        return 4.5


class Mocha(Coffee):
    def get_name(self):
        return "Мокка"

    def get_ingredients(self):
        return ["кофе", "вода", "шоколад", "молоко"]

    def get_cost(self):
        return 5.0


# Абстрактный класс фабрики
class CoffeeFactory(ABC):
    @abstractmethod
    def create_coffee(self):
        pass


# Конкретные фабрики для каждого напитка
class EspressoFactory(CoffeeFactory):
    def create_coffee(self):
        return Espresso()


class AmericanoFactory(CoffeeFactory):
    def create_coffee(self):
        return Americano()


class CappuccinoFactory(CoffeeFactory):
    def create_coffee(self):
        return Cappuccino()


class LatteFactory(CoffeeFactory):
    def create_coffee(self):
        return Latte()


class MochaFactory(CoffeeFactory):
    def create_coffee(self):
        return Mocha()


# Класс кофе-автомата
class CoffeeMachine:
    def make_coffee(self, factory):
        coffee = factory.create_coffee()
        print(f"Готовим {coffee.get_name()}...")
        print(f"Ингредиенты: {', '.join(coffee.get_ingredients())}")
        print(f"Стоимость: ${coffee.get_cost()}")
        return coffee


# Словарь для соответствия выбора пользователя и фабрик
COFFEE_TYPES = {
    '1': ('Эспрессо', EspressoFactory()),
    '2': ('Американо', AmericanoFactory()),
    '3': ('Капучино', CappuccinoFactory()),
    '4': ('Латте', LatteFactory()),
    '5': ('Мокка', MochaFactory())
}


# Функция для отображения меню
def show_menu():
    print("\n=== Меню кофейни ===")
    for key, (name, _) in COFFEE_TYPES.items():
        coffee = COFFEE_TYPES[key][1].create_coffee()
        print(f"{key}. {name} - ${coffee.get_cost()}")
    print("0. Выход")


# Демонстрация работы
def main():
    machine = CoffeeMachine()

    while True:
        show_menu()
        choice = input("\nВыберите кофе (0-5): ").strip()

        if choice == '0':
            print("Спасибо за визит!")
            break

        if choice not in COFFEE_TYPES:
            print("Неверный выбор, попробуйте снова.")
            continue

        coffee_name, factory = COFFEE_TYPES[choice]
        print(f"\nВы выбрали: {coffee_name}")
        machine.make_coffee(factory)


if __name__ == "__main__":
    main()

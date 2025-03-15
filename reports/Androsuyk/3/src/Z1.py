from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Espresso(Coffee):
    def prepare(self):
        return "Espresso: крепкий кофе без молока!"

class Latte(Coffee):
    def prepare(self):
        return "Latte: эспрессо с молоком и молочной пенкой!"

class Cappuccino(Coffee):
    def prepare(self):
        return "Cappuccino: эспрессо с большим количеством молочной пенки!"

class Americano(Coffee):
    def prepare(self):
        return "Americano: эспрессо с добавлением горячей воды!"

class Mocha(Coffee):
    def prepare(self):
        return "Mocha: эспрессо с шоколадом и молоком!"


class CoffeeFactory(ABC):
    @abstractmethod
    def create_coffee(self) -> Coffee:
        pass


class EspressoFactory(CoffeeFactory):
    def create_coffee(self) -> Coffee:
        return Espresso()

class LatteFactory(CoffeeFactory):
    def create_coffee(self) -> Coffee:
        return Latte()

class CappuccinoFactory(CoffeeFactory):
    def create_coffee(self) -> Coffee:
        return Cappuccino()

class AmericanoFactory(CoffeeFactory):
    def create_coffee(self) -> Coffee:
        return Americano()

class MochaFactory(CoffeeFactory):
    def create_coffee(self) -> Coffee:
        return Mocha()


class CoffeeMachine:
    def __init__(self):
        self.factories = {
            "1": EspressoFactory(),
            "2": LatteFactory(),
            "3": CappuccinoFactory(),
            "4": AmericanoFactory(),
            "5": MochaFactory(),
        }

    def make_coffee(self, choice):
        factory = self.factories.get(choice)
        if factory:
            coffee = factory.create_coffee()
            print(coffee.prepare())
        else:
            print("Ошибка.")


def display_menu():
    print("Выберите кофе:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Americano")
    print("5. Mocha")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    while True:
        display_menu()
        _choice = input("Введите номер кофе или 'q', если нужно выйти: ").strip()

        if _choice.lower() == 'q':
            print("Выход")
            break

        coffee_machine.make_coffee(_choice)

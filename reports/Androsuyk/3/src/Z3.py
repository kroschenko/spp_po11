from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def press(self):
        pass


class FixedButton(Button):
    def __init__(self, label, action):
        self.label = label
        self.action = action

    def press(self):
        print(f"Нажата кнопка '{self.label}': {self.action}")
        return self.action


class ConfigurableButton(Button):
    def __init__(self, label):
        self.label = label
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def press(self):
        if self.strategy:
            result = self.strategy.execute()
            print(f"Нажата кнопка '{self.label}': {result}")
            return result
        else:
            print(f"Кнопка '{self.label}' не настроена.")
            return None


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ClearStrategy(Strategy):
    def execute(self):
        return "Очистка экрана..."


class MemorySaveStrategy(Strategy):
    def execute(self):
        return "Сохранение в память..."


class MemoryRecallStrategy(Strategy):
    def execute(self):
        return "Извлечение из памяти..."


class SquareRootStrategy(Strategy):
    def execute(self):
        return "Вычисление квадратного корня..."


class PercentageStrategy(Strategy):
    def execute(self):
        return "Вычисление процента..."


class Keyboard:
    def __init__(self):
        self.buttons = {}

    def add_button(self, name, button):
        self.buttons[name] = button

    def press_button(self, name):
        if name in self.buttons:
            return self.buttons[name].press()
        else:
            print(f"Кнопка '{name}' не найдена.")
            return None

    def list_buttons(self):
        print("Доступные кнопки:")
        for name in self.buttons:
            print(f"- {name}")


def display_menu():
    print("\nМеню:")
    print("1. Нажать кнопку")
    print("2. Назначить функцию настраиваемой кнопке")
    print("3. Список кнопок")
    print("4. Выйти")


if __name__ == "__main__":
    keyboard = Keyboard()

    keyboard.add_button("1", FixedButton("1", "Ввод цифры 1"))
    keyboard.add_button("2", FixedButton("2", "Ввод цифры 2"))
    keyboard.add_button("+", FixedButton("+", "Сложение"))
    keyboard.add_button("-", FixedButton("-", "Вычитание"))

    config_button_a = ConfigurableButton("A")
    config_button_b = ConfigurableButton("B")

    keyboard.add_button("A", config_button_a)
    keyboard.add_button("B", config_button_b)


    strategies = {
        "1": ClearStrategy(),
        "2": MemorySaveStrategy(),
        "3": MemoryRecallStrategy(),
        "4": SquareRootStrategy(),
        "5": PercentageStrategy(),
    }

    while True:
        display_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":  
            button_name = input("Введите название кнопки: ").strip()
            keyboard.press_button(button_name)

        elif choice == "2":  
            button_name = input("Введите название настраиваемой кнопки (A или B): ").strip().upper()
            if button_name in ["A", "B"]:
                print("Доступные функции:")
                for key, strategy in strategies.items():
                    print(f"{key}. {strategy.execute()}")
                strategy_choice = input("Выберите функцию (1-5): ").strip()
                if strategy_choice in strategies:
                    if button_name == "A":
                        config_button_a.set_strategy(strategies[strategy_choice])
                    elif button_name == "B":
                        config_button_b.set_strategy(strategies[strategy_choice])
                    print(f"Функция назначена на кнопку '{button_name}'.")
                else:
                    print("Неверный выбор функции.")
            else:
                print("Неверное название кнопки.")

        elif choice == "3":  
            keyboard.list_buttons()

        elif choice == "4":  
            print("Выход")
            break

        else:
            print("Ошибка.")

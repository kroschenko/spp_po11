from abc import ABC, abstractmethod
import math

# Интерфейс команды
class Command(ABC):
    @abstractmethod
    def execute(self, calculator):
        pass

# Класс калькулятора
class Calculator:
    def __init__(self):
        self.value = 0  # текущее значение

    def set_value(self, value):
        self.value = value
        print(f"Новое значение: {self.value}")

    def add(self, x):
        self.value += x
        print(f"Сложение: {self.value}")

    def multiply(self, x):
        self.value *= x
        print(f"Умножение: {self.value}")

    def sine(self):
        self.value = math.sin(self.value)
        print(f"Синус: {self.value}")

    def power(self, x):
        self.value = self.value ** x
        print(f"Возведение в степень: {self.value}")

# Конкретные команды
class NumberCommand(Command):
    def __init__(self, number):
        self.number = number

    def execute(self, calculator):
        calculator.set_value(self.number)

class AddCommand(Command):
    def __init__(self, number):
        self.number = number

    def execute(self, calculator):
        calculator.add(self.number)

class MultiplyCommand(Command):
    def __init__(self, number):
        self.number = number

    def execute(self, calculator):
        calculator.multiply(self.number)

class SineCommand(Command):
    def execute(self, calculator):
        calculator.sine()

class PowerCommand(Command):
    def __init__(self, exponent):
        self.exponent = exponent

    def execute(self, calculator):
        calculator.power(self.exponent)

# Класс кнопки
class Button:
    def __init__(self, name):
        self.name = name
        self.command = None  # команда, привязанная к кнопке

    def set_command(self, command):
        self.command = command
        print(f"Кнопке {self.name} назначена команда")

    def press(self, calculator):
        if self.command:
            print(f"Нажимаем кнопку {self.name}...")
            self.command.execute(calculator)
        else:
            print(f"Кнопка {self.name} не настроена")

# Класс клавиатуры
class Keyboard:
    def __init__(self):
        self.buttons = {}

    def add_button(self, name, command=None):
        button = Button(name)
        if command:
            button.set_command(command)
        self.buttons[name] = button

    def press_button(self, name, calculator):
        if name in self.buttons:
            self.buttons[name].press(calculator)
        else:
            print(f"Кнопка {name} не существует")

# Демонстрация работы
def main():
    calc = Calculator()
    keyboard = Keyboard()

    # Фиксированные кнопки (цифровые и арифметические)
    keyboard.add_button("1", NumberCommand(1))
    keyboard.add_button("5", NumberCommand(5))
    keyboard.add_button("Add_2", AddCommand(2))
    keyboard.add_button("Multiply_3", MultiplyCommand(3))

    # Настраиваемые кнопки
    keyboard.add_button("Func1")
    keyboard.add_button("Func2")

    # Меню для пользователя
    fixed_commands = {
        '1': ('Установить 1', '1'),
        '2': ('Установить 5', '5'),
        '3': ('Сложить 2', 'Add_2'),
        '4': ('Умножить на 3', 'Multiply_3')
    }

    configurable_commands = {
        '1': ('Синус', SineCommand()),
        '2': ('Возвести в степень 2', PowerCommand(2))
    }

    def show_menu():
        print("\n=== Меню калькулятора ===")
        print("Фиксированные команды:")
        for key, (desc, _) in fixed_commands.items():
            print(f"{key}. {desc}")
        print("\nНастраиваемые кнопки:")
        print("5. Назначить команду для Func1")
        print("6. Назначить команду для Func2")
        print("7. Нажать Func1")
        print("8. Нажать Func2")
        print("0. Выход")

    def show_configurable_menu():
        print("\n=== Выберите команду для кнопки ===")
        for key, (desc, _) in configurable_commands.items():
            print(f"{key}. {desc}")

    while True:
        show_menu()
        choice = input("\nВыберите действие (0-8): ").strip()

        if choice == '0':
            print("Выход из программы.")
            break

        if choice in fixed_commands:
            _, button_name = fixed_commands[choice]
            keyboard.press_button(button_name, calc)
            continue

        if choice in ['5', '6']:
            button_name = "Func1" if choice == '5' else "Func2"
            show_configurable_menu()
            config_choice = input("\nВыберите команду (1-2): ").strip()

            if config_choice in configurable_commands:
                _, command = configurable_commands[config_choice]
                keyboard.buttons[button_name].set_command(command)
            else:
                print("Неверный выбор команды.")
            continue

        if choice in ['7', '8']:
            button_name = "Func1" if choice == '7' else "Func2"
            keyboard.press_button(button_name, calc)
            continue

        print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, text: str):
        pass


class LaserPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Лазерная печать] {text}")


class InkjetPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Струйная печать] {text}")


class MatrixPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Матричная печать] {text}")


class Printer:
    def __init__(self, name: str):
        self.name = name
        self.strategy = None

    def set_print_type(self, strategy: PrintStrategy):
        self.strategy = strategy

    def do_print(self, text: str):
        print(f"\nПринтер '{self.name}' готов к печати:")
        if self.strategy:
            self.strategy.print(text)
        else:
            print("Ошибка: не выбран тип печати!")


def show_printers_menu(printers):
    print("\nДоступные принтеры:")
    for i, printer in enumerate(printers, 1):
        print(f"{i}. {printer.name}")
    return input("Номер принтера: ")


def show_types_menu():
    print("\nТипы печати:")
    print("1. Лазерная")
    print("2. Струйная")
    print("3. Матричная")
    return input("Номер типа печати: ")


def handle_printer_selection(printers):
    try:
        choice = int(input) - 1
        if 0 <= choice < len(printers):
            return printers[choice]
        print("Ошибка: неверный номер принтера")
    except ValueError:
        print("Ошибка: введите число")
    return None


def handle_type_selection(print_types, printer):
    try:
        choice = int(input)
        if choice in print_types:
            printer.set_print_type(print_types[choice])
            print("Тип печати установлен")
            return True
        print("Ошибка: неверный тип печати")
    except ValueError:
        print("Ошибка: введите число")
    return False


def main():
    printers = [
        Printer("Офисный HP"),
        Printer("Домашний Canon"),
        Printer("Магазинный Epson")
    ]

    print_types = {
        1: LaserPrint(),
        2: InkjetPrint(),
        3: MatrixPrint()
    }

    current_printer = None

    while True:
        print("\n=== Меню управления принтерами ===")
        print("1. Выбрать принтер")
        print("2. Выбрать тип печати")
        print("3. Напечатать текст")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            current_printer = handle_printer_selection(printers)
        elif choice == "2":
            if current_printer:
                handle_type_selection(print_types, current_printer)
            else:
                print("Сначала выберите принтер!")
        elif choice == "3":
            if current_printer:
                current_printer.do_print(input("Введите текст для печати: "))
            else:
                print("Сначала выберите принтер!")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()

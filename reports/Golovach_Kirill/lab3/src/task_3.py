from abc import ABC, abstractmethod
import time


# Интерфейс состояния
class PrinterState(ABC):
    @abstractmethod
    def print_document(self, printer):
        pass

    @abstractmethod
    def load_paper(self, printer):
        pass

    @abstractmethod
    def remove_jammed_paper(self, printer):
        pass

    @abstractmethod
    def refill_cartridge(self, printer):
        pass


# Конкретные состояния
class IdleState(PrinterState):
    def print_document(self, printer):
        if printer.paper_count > 0 and printer.ink_level > 0:
            print("Начало печати...")
            printer.set_state(PrintingState())
            printer.print_document()  # Переходим в состояние печати
        elif printer.paper_count == 0:
            print("Отказ: нет бумаги!")
            printer.set_state(OutOfPaperState())
        elif printer.ink_level == 0:
            print("Чистый лист выдан (нет чернил).")
            printer.paper_count -= 1
            printer.set_state(IdleState())

    def load_paper(self, printer):
        print(f"Загрузка бумаги. Было {printer.paper_count} листов.")
        printer.paper_count += 50  # Загружаем 50 листов
        print(f"Теперь {printer.paper_count} листов.")

    def remove_jammed_paper(self, printer):
        print("Зажатой бумаги нет.")

    def refill_cartridge(self, printer):
        print("Картридж заправлен.")
        printer.ink_level = 100


class PrintingState(PrinterState):
    def print_document(self, printer):
        print("Процесс печати...")
        time.sleep(1)  # Имитация времени печати
        printer.paper_count -= 1
        printer.ink_level -= 10  # На одну страницу уходит 10% чернил
        printer.print_count += 1  # Увеличиваем счетчик печатей
        print("Документ напечатан.")

        # Проверяем, нужно ли зажевать бумагу
        if printer.print_count % 2 == 0:
            print("Бумага зажевалась!")
            printer.set_state(PaperJamState())
        else:
            printer.set_state(IdleState())

    def load_paper(self, printer):
        print("Операция недоступна во время печати.")

    def remove_jammed_paper(self, printer):
        print("Операция недоступна во время печати.")

    def refill_cartridge(self, printer):
        print("Операция недоступна во время печати.")


class PaperJamState(PrinterState):
    def print_document(self, printer):
        print("Операция недоступна при зажатии бумаги.")

    def load_paper(self, printer):
        print("Операция недоступна при зажатии бумаги.")

    def remove_jammed_paper(self, printer):
        print("Извлечение зажатой бумаги...")
        printer.set_state(IdleState())

    def refill_cartridge(self, printer):
        print("Операция недоступна при зажатии бумаги.")


class OutOfPaperState(PrinterState):
    def print_document(self, printer):
        print("Отказ: нет бумаги!")

    def load_paper(self, printer):
        print(f"Загрузка бумаги. Было {printer.paper_count} листов.")
        printer.paper_count += 50  # Загружаем 50 листов
        print(f"Теперь {printer.paper_count} листов.")
        printer.set_state(IdleState())

    def remove_jammed_paper(self, printer):
        print("Зажатой бумаги нет.")

    def refill_cartridge(self, printer):
        print("Операция недоступна при отсутствии бумаги.")


# Контекст (Принтер)
class Printer:
    def __init__(self, model, paper_count=10, ink_level=100):
        self.model = model
        self.paper_count = paper_count
        self.ink_level = ink_level
        self.state = IdleState()
        self.print_count = 0  # Счетчик успешных печатей

    def set_state(self, state):
        self.state = state

    def print_document(self):
        self.state.print_document(self)

    def load_paper(self):
        self.state.load_paper(self)

    def remove_jammed_paper(self):
        self.state.remove_jammed_paper(self)

    def refill_cartridge(self):
        self.state.refill_cartridge(self)


# Функция для вывода меню и обработки выбора пользователя
def main():
    printer = Printer(model="HP LaserJet Pro", paper_count=10, ink_level=100)

    while True:
        print("\n=== Меню принтера ===")
        print("1. Печать документа")
        print("2. Загрузка бумаги")
        print("3. Извлечение зажатой бумаги")
        print("4. Заправка картриджа")
        print("5. Выход")
        print(f"Текущее состояние: {printer.state.__class__.__name__}")
        print(f"Бумага: {printer.paper_count}, Чернила: {printer.ink_level}%")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            printer.print_document()
        elif choice == "2":
            printer.load_paper()
        elif choice == "3":
            printer.remove_jammed_paper()
        elif choice == "4":
            printer.refill_cartridge()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
    
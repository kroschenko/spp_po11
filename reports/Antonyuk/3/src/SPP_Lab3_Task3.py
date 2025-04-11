from abc import ABC, abstractmethod

# Базовый класс для печати
class PrintStrategy(ABC):
    @abstractmethod
    def print(self, text: str):
        pass

# Конкретные типы печати
class LaserPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Лазерная печать] {text}")

class InkjetPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Струйная печать] {text}")

class MatrixPrint(PrintStrategy):
    def print(self, text: str):
        print(f"[Матричная печать] {text}")

# Класс принтера
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

# Главное меню
def main():
    # Создаем список принтеров
    printers = [
        Printer("Офисный HP"),
        Printer("Домашний Canon"),
        Printer("Магазинный Epson")
    ]
    
    # Создаем типы печати
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
            print("\nДоступные принтеры:")
            for i, printer in enumerate(printers, 1):
                print(f"{i}. {printer.name}")
            
            try:
                num = int(input("Номер принтера: ")) - 1
                current_printer = printers[num]
                print(f"Выбран: {current_printer.name}")
            except:
                print("Ошибка выбора!")
        
        elif choice == "2":
            if not current_printer:
                print("Сначала выберите принтер!")
                continue
                
            print("\nТипы печати:")
            print("1. Лазерная")
            print("2. Струйная")
            print("3. Матричная")
            
            try:
                num = int(input("Номер типа печати: "))
                current_printer.set_print_type(print_types[num])
                print("Тип печати установлен")
            except:
                print("Ошибка выбора!")
        
        elif choice == "3":
            if not current_printer:
                print("Сначала выберите принтер!")
                continue
                
            text = input("Введите текст для печати: ")
            current_printer.do_print(text)
        
        elif choice == "0":
            print("До свидания!")
            break
        
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()

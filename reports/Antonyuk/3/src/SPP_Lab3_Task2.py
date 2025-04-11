from abc import ABC, abstractmethod
from datetime import date
from typing import List, Dict, Type

class CardComponent(ABC):
    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def edit(self):
        pass

class PassportComponent(CardComponent):
    def __init__(self):
        self.full_name = ""
        self.birth_date = None
        self.passport_number = ""
        self.issue_date = None
        self.expiry_date = None

    def show_info(self):
        print("\n=== Паспортные данные ===")
        print(f"1. ФИО: {self.full_name}")
        print(f"2. Дата рождения: {self.birth_date}")
        print(f"3. Номер паспорта: {self.passport_number}")
        print(f"4. Дата выдачи: {self.issue_date}")
        print(f"5. Срок действия: {self.expiry_date}")
        print(f"Действителен: {'Да' if self.is_valid() else 'Нет'}")

    def is_valid(self) -> bool:
        return self.expiry_date and date.today() <= self.expiry_date

    def edit(self):
        print("\nРедактирование паспортных данных:")
        self.full_name = input("Введите ФИО: ") or self.full_name
        self.birth_date = self._input_date("Дата рождения (ГГГГ-ММ-ДД): ", self.birth_date)
        self.passport_number = input("Номер паспорта: ") or self.passport_number
        self.issue_date = self._input_date("Дата выдачи (ГГГГ-ММ-ДД): ", self.issue_date)
        self.expiry_date = self._input_date("Срок действия (ГГГГ-ММ-ДД): ", self.expiry_date)

    def _input_date(self, prompt, current_value=None):
        while True:
            date_str = input(prompt) or (str(current_value) if current_value else "")
            if not date_str:
                return current_value
            try:
                return date.fromisoformat(date_str)
            except ValueError:
                print("Неверный формат даты. Используйте ГГГГ-ММ-ДД")

class InsuranceComponent(CardComponent):
    def __init__(self):
        self.policy_number = ""
        self.insurance_company = ""
        self.expiry_date = None

    def show_info(self):
        print("\n=== Страховой полис ===")
        print(f"1. Номер полиса: {self.policy_number}")
        print(f"2. Страховая компания: {self.insurance_company}")
        print(f"3. Срок действия: {self.expiry_date}")
        print(f"Действителен: {'Да' if self.is_valid() else 'Нет'}")

    def is_valid(self) -> bool:
        return self.expiry_date and date.today() <= self.expiry_date

    def edit(self):
        print("\nРедактирование страхового полиса:")
        self.policy_number = input("Номер полиса: ") or self.policy_number
        self.insurance_company = input("Страховая компания: ") or self.insurance_company
        self.expiry_date = self._input_date("Срок действия (ГГГГ-ММ-ДД): ", self.expiry_date)

    def _input_date(self, prompt, current_value=None):
        while True:
            date_str = input(prompt) or (str(current_value) if current_value else "")
            if not date_str:
                return current_value
            try:
                return date.fromisoformat(date_str)
            except ValueError:
                print("Неверный формат даты. Используйте ГГГГ-ММ-ДД")

class BankCardComponent(CardComponent):
    def __init__(self):
        self.card_number = ""
        self.bank_name = ""
        self.expiry_date = None
        self.balance = 0.0

    def show_info(self):
        print("\n=== Банковская карта ===")
        print(f"1. Номер карты: **** **** **** {self.card_number[-4:] if self.card_number else '****'}")
        print(f"2. Банк: {self.bank_name}")
        print(f"3. Срок действия: {self.expiry_date}")
        print(f"4. Баланс: {self.balance:.2f} руб.")
        print(f"Действительна: {'Да' if self.is_valid() else 'Нет'}")

    def is_valid(self) -> bool:
        return self.expiry_date and date.today() <= self.expiry_date

    def edit(self):
        print("\nРедактирование банковской карты:")
        self.card_number = input("Номер карты (16 цифр): ") or self.card_number
        self.bank_name = input("Название банка: ") or self.bank_name
        self.expiry_date = self._input_date("Срок действия (ГГГГ-ММ-ДД): ", self.expiry_date)
        self._input_balance()

    def _input_date(self, prompt, current_value=None):
        while True:
            date_str = input(prompt) or (str(current_value) if current_value else "")
            if not date_str:
                return current_value
            try:
                return date.fromisoformat(date_str)
            except ValueError:
                print("Неверный формат даты. Используйте ГГГГ-ММ-ДД")

    def _input_balance(self):
        while True:
            balance_str = input(f"Баланс ({self.balance:.2f}): ") or str(self.balance)
            try:
                self.balance = float(balance_str)
                break
            except ValueError:
                print("Неверный формат суммы. Используйте число (например 1000.50)")

class UniversalElectronicCard:
    def __init__(self):
        self.components: Dict[str, CardComponent] = {
            "1": PassportComponent(),
            "2": InsuranceComponent(),
            "3": BankCardComponent()
        }

    def show_info(self):
        print("\n=== Универсальная электронная карта ===")
        for name, component in self.components.items():
            component.show_info()

    def edit_component(self):
        print("\nВыберите компонент для редактирования:")
        print("1. Паспортные данные")
        print("2. Страховой полис")
        print("3. Банковская карта")
        print("0. Назад")
        
        choice = input("Ваш выбор: ")
        if choice in self.components:
            self.components[choice].edit()
        elif choice != "0":
            print("Неверный выбор")

    def is_valid(self) -> bool:
        return all(component.is_valid() for component in self.components.values())

def main():
    card = UniversalElectronicCard()
    
    while True:
        print("\n=== Меню управления электронной картой ===")
        print("1. Просмотреть данные карты")
        print("2. Редактировать данные")
        print("3. Проверить валидность карты")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            card.show_info()
        elif choice == "2":
            card.edit_component()
        elif choice == "3":
            valid = card.is_valid()
            print(f"\nКарта {'действительна' if valid else 'недействительна'}")
            if not valid:
                print("Проверьте сроки действия компонентов")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()

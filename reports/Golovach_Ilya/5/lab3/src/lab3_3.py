from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm: 'ATM') -> None:
        pass

    @abstractmethod
    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        pass

    @abstractmethod
    def withdraw(self, atm: 'ATM', amount: float) -> None:
        pass

    @abstractmethod
    def eject_card(self, atm: 'ATM') -> None:
        pass

    @abstractmethod
    def display_menu(self, atm: 'ATM') -> None:
        pass

class IdleState(ATMState):
    def insert_card(self, atm: 'ATM') -> None:
        print("\nКарта вставлена. Введите PIN.")
        atm.set_state(AuthenticationState())

    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        print("\nОшибка: Сначала вставьте карту.")

    def withdraw(self, atm: 'ATM', amount: float) -> None:
        print("\nОшибка: Сначала вставьте карту и введите PIN.")

    def eject_card(self, atm: 'ATM') -> None:
        print("\nОшибка: Карта не вставлена.")

    def display_menu(self, atm: 'ATM') -> None:
        print("\n=== Меню ===")
        print("1. Вставить карту")
        print("2. Проверить баланс банкомата")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            self.insert_card(atm)
        elif choice == "2":
            print(f"\nОбщий баланс банкомата: {atm.total_cash} рублей")
        elif choice == "3":
            print("До свидания!")
            exit()
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

class AuthenticationState(ATMState):
    def insert_card(self, atm: 'ATM') -> None:
        print("\nОшибка: Карта уже вставлена.")

    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        if pin == "1234":  # Пример правильного PIN
            print("\nPIN верный. Выберите операцию.")
            atm.set_state(OperationState())
        else:
            print("\nНеверный PIN. Попробуйте ещё раз.")

    def withdraw(self, atm: 'ATM', amount: float) -> None:
        print("\nОшибка: Сначала введите PIN.")

    def eject_card(self, atm: 'ATM') -> None:
        print("\nКарта извлечена.")
        atm.set_state(IdleState())

    def display_menu(self, atm: 'ATM') -> None:
        print("\n=== Меню ===")
        print("1. Ввести PIN")
        print("2. Извлечь карту")
        print("3. Проверить баланс банкомата")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            pin = input("Введите PIN: ")
            self.enter_pin(atm, pin)
        elif choice == "2":
            self.eject_card(atm)
        elif choice == "3":
            print(f"\nОбщий баланс банкомата: {atm.total_cash} рублей")
        elif choice == "4":
            print("До свидания!")
            exit()
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

class OperationState(ATMState):
    def insert_card(self, atm: 'ATM') -> None:
        print("\nОшибка: Карта уже вставлена.")

    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        print("\nОшибка: PIN уже введён.")

    def withdraw(self, atm: 'ATM', amount: float) -> None:
        if amount <= atm.total_cash:
            print(f"\nВыдано {amount} рублей.")
            atm.total_cash -= amount
            print(f"Остаток в банкомате: {atm.total_cash} рублей")
            atm.set_state(IdleState())
        else:
            print("\nНедостаточно средств. Банкомат заблокирован.")
            atm.set_state(BlockedState())

    def eject_card(self, atm: 'ATM') -> None:
        print("\nКарта извлечена.")
        atm.set_state(IdleState())

    def display_menu(self, atm: 'ATM') -> None:
        print("\n=== Меню ===")
        print("1. Снять деньги")
        print("2. Проверить баланс банкомата")
        print("3. Извлечь карту")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            try:
                amount = float(input("Введите сумму для снятия: "))
                self.withdraw(atm, amount)
            except ValueError:
                print("Неверный ввод. Введите число.")
        elif choice == "2":
            print(f"\nОбщий баланс банкомата: {atm.total_cash} рублей")
        elif choice == "3":
            self.eject_card(atm)
        elif choice == "4":
            print("До свидания!")
            exit()
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

class BlockedState(ATMState):
    def insert_card(self, atm: 'ATM') -> None:
        print("\nОшибка: Банкомат заблокирован. Обратитесь в банк.")

    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        print("\nОшибка: Банкомат заблокирован. Обратитесь в банк.")

    def withdraw(self, atm: 'ATM', amount: float) -> None:
        print("\nОшибка: Банкомат заблокирован. Обратитесь в банк.")

    def eject_card(self, atm: 'ATM') -> None:
        print("\nКарта извлечена. Банкомат остаётся заблокированным.")
        atm.set_state(IdleState())

    def display_menu(self, atm: 'ATM') -> None:
        print("\n=== Меню ===")
        print("1. Извлечь карту")
        print("2. Проверить баланс банкомата")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            self.eject_card(atm)
        elif choice == "2":
            print(f"\nОбщий баланс банкомата: {atm.total_cash} рублей")
        elif choice == "3":
            print("До свидания!")
            exit()
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

class ATM:
    def __init__(self, atm_id: str, total_cash: float):
        self.atm_id = atm_id
        self.total_cash = total_cash  # Общая сумма денег в банкомате
        self.state: ATMState = IdleState()

    def set_state(self, state: ATMState) -> None:
        self.state = state

    def insert_card(self) -> None:
        self.state.insert_card(self)

    def enter_pin(self, pin: str) -> None:
        self.state.enter_pin(self, pin)

    def withdraw(self, amount: float) -> None:
        self.state.withdraw(self, amount)

    def eject_card(self) -> None:
        self.state.eject_card(self)

    def display_menu(self) -> None:
        self.state.display_menu(self)

def main():
    atm = ATM("ATM-001", 10000.0)
    print("Добро пожаловать в банкомат!")
    while True:
        atm.display_menu()

if __name__ == "__main__":
    main()
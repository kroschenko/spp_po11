from abc import ABC, abstractmethod


class ATM:
    def __init__(self, atm_id, total_money):
        self.atm_id = atm_id
        self.total_money = total_money
        self.correct_pin = "1234"
        self.state: ATMState = WaitingState(self)

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card()

    def enter_pin(self, entered_pin):
        self.state.enter_pin(entered_pin)

    def withdraw(self, withdraw_amount):
        self.state.withdraw(withdraw_amount)

    def finish(self):
        self.state.finish()


class ATMState(ABC):
    def __init__(self, atm_machine: ATM):
        self.atm = atm_machine

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self, entered_pin):
        pass

    @abstractmethod
    def withdraw(self, withdraw_amount):
        pass

    @abstractmethod
    def finish(self):
        pass


class WaitingState(ATMState):
    def insert_card(self):
        print("Карта вставлена. Введите PIN.")
        self.atm.set_state(AuthenticationState(self.atm))

    def enter_pin(self, entered_pin):
        print("Вставьте карту сначала.")

    def withdraw(self, withdraw_amount):
        print("Невозможно снять деньги. Нет карты.")

    def finish(self):
        print("Нет активной сессии.")


class AuthenticationState(ATMState):
    def insert_card(self):
        print("Карта уже вставлена.")

    def enter_pin(self, entered_pin):
        if entered_pin == self.atm.correct_pin:
            print("ПИН-код верный.")
            self.atm.set_state(OperationState(self.atm))
        else:
            print("Неверный ПИН-код.")
            self.atm.set_state(WaitingState(self.atm))

    def withdraw(self, withdraw_amount):
        print("Сначала введите ПИН.")

    def finish(self):
        print("Сначала введите ПИН.")


class OperationState(ATMState):
    def insert_card(self):
        print("Операция уже выполняется.")

    def enter_pin(self, entered_pin):
        print("ПИН уже введён.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.atm.total_money:
            self.atm.total_money -= withdraw_amount
            print(f"Выдано: {withdraw_amount}. Остаток: {self.atm.total_money}")
            if self.atm.total_money == 0:
                print("Банкомат пуст. Блокировка.")
                self.atm.set_state(BlockedState(self.atm))
        else:
            print("Недостаточно средств в банкомате.")

    def finish(self):
        print("Сессия завершена.")
        self.atm.set_state(WaitingState(self.atm))


class BlockedState(ATMState):
    def insert_card(self):
        print("Банкомат заблокирован. Недостаточно средств.")

    def enter_pin(self, entered_pin):
        print("Банкомат заблокирован.")

    def withdraw(self, withdraw_amount):
        print("Невозможно выполнить операцию. Банкомат пуст.")

    def finish(self):
        print("Банкомат заблокирован.")


if __name__ == "__main__":
    atm = ATM(atm_id="1", total_money=500)

    while True:
        print("1. Вставить карту")
        print("2. Ввести ПИН-код")
        print("3. Снять деньги")
        print("4. Завершить сессию")
        print("0. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            atm.insert_card()
        elif choice == "2":
            user_pin = input("Введите ПИН-код: ")
            atm.enter_pin(user_pin)
        elif choice == "3":
            try:
                withdraw_amount = int(input("Введите сумму для снятия: "))
                atm.withdraw(withdraw_amount)
            except ValueError:
                print("Ошибка ввода суммы. Введите число.")
        elif choice == "4":
            atm.finish()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

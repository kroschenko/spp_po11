import sys


class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self._account_number = account_number
        self._balance = balance
        self._is_active = True

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def is_active(self):
        return self._is_active

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if not self._is_active:
            raise ValueError("Счет не активен")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if not self._is_active:
            raise ValueError("Счет не активен")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def close_account(self):
        self._is_active = False
        self._balance = 0

    def __str__(self):
        status = "активен" if self._is_active else "неактивен"
        return f"Счет №{self._account_number}, баланс: {self._balance:.2f}, статус: {status}"


class CreditCard:
    def __init__(self, card_number, credit_limit=10000.0):
        self._card_number = card_number
        self._credit_limit = credit_limit
        self._current_credit = 0.0
        self._is_blocked = False

    @property
    def card_number(self):
        return self._card_number

    @property
    def credit_limit(self):
        return self._credit_limit

    @property
    def current_credit(self):
        return self._current_credit

    @property
    def is_blocked(self):
        return self._is_blocked

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self._is_blocked:
            raise ValueError("Карта заблокирована")
        if amount > (self._credit_limit - self._current_credit):
            raise ValueError("Превышен кредитный лимит")
        self._current_credit += amount

    def repay_credit(self, amount):
        amount = min(amount, self._current_credit)
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._current_credit -= amount

    def block_card(self):
        self._is_blocked = True

    def unblock_card(self):
        if self._current_credit <= 0:
            self._is_blocked = False

    def __str__(self):
        status = "заблокирована" if self._is_blocked else "активна"
        return (f"Карта №{self._card_number}, лимит: {self._credit_limit:.2f}, "
                f"кредит: {self._current_credit:.2f}, статус: {status}")


class Client:
    def __init__(self, name, account, credit_card):
        self._name = name
        self._account = account
        self._credit_card = credit_card

    @property
    def name(self):
        return self._name

    @property
    def credit_card_info(self):
        """Геттер для информации о кредитной карте"""
        return {
            'current_credit': self._credit_card.current_credit,
            'credit_limit': self._credit_card.credit_limit,
            'card': self._credit_card
        }

    def pay_order(self, merchant_name, amount, use_credit=False):
        """Оплатить заказ"""
        if use_credit:
            try:
                self._credit_card.make_payment(amount)
                print(f"Оплачено {amount:.2f} с кредитной карты для {merchant_name}")
            except ValueError as e:
                print(f"Ошибка оплаты: {e}")
        else:
            try:
                self._account.withdraw(amount)
                print(f"Оплачено {amount:.2f} со счета для {merchant_name}")
            except ValueError as e:
                print(f"Ошибка оплаты: {e}")

    def transfer_to_account(self, target_account_number, amount):
        """Перевести деньги на другой счет"""
        try:
            target_account = BankAccount(target_account_number)
            self._account.withdraw(amount)
            target_account.deposit(amount)
            print(f"Переведено {amount:.2f} на счет {target_account_number}")
        except ValueError as e:
            print(f"Ошибка перевода: {e}")

    def block_credit_card(self):
        """Заблокировать кредитную карту"""
        self._credit_card.block_card()
        print("Кредитная карта заблокирована клиентом")

    def close_account(self):
        """Аннулировать счет"""
        self._account.close_account()
        print("Счет аннулирован")

    def __str__(self):
        return f"Клиент: {self._name}\n{self._account}\n{self._credit_card}"


class Administrator:
    @staticmethod
    def get_excess_status(client):
        """Проверка превышения кредитного лимита"""
        card_info = client.credit_card_info
        return (card_info['current_credit'] > card_info['credit_limit'],
                card_info['card'])

    @staticmethod
    def block_card_for_excess(client):
        """Блокировка карты за превышение лимита"""
        is_exceeded, card = Administrator.get_excess_status(client)
        if is_exceeded:
            card.block_card()
            print("\n[АДМИНИСТРАТОР] Карта заблокирована за превышение кредитного лимита!")
            return True
        return False


def input_float(prompt):
    """Ввод числа с плавающей точкой"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Значение должно быть положительным!")
                continue
            return value
        except ValueError:
            print("Пожалуйста, введите число!")


def input_int(prompt):
    """Ввод целого числа"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите целое число!")


def create_client():
    """Создание нового клиента"""
    print("\n=== СОЗДАНИЕ НОВОГО КЛИЕНТА ===")
    name = input("Введите имя клиента: ")
    account_num = input("Введите номер счета (цифры): ")
    balance = input_float("Введите начальный баланс счета: ")
    card_num = input("Введите номер кредитной карты (16 цифр): ")
    credit_limit = input_float("Введите кредитный лимит: ")

    account = BankAccount(account_num, balance)
    card = CreditCard(card_num, credit_limit)
    return Client(name, account, card)


def handle_payment(client):
    """Обработка операции оплаты"""
    merchant = input("Введите название магазина/услуги: ")
    amount = input_float("Введите сумму оплаты: ")
    use_credit = input("Использовать кредитную карту? (y/n): ").lower() == 'y'
    client.pay_order(merchant, amount, use_credit)


def handle_transfer(client):
    """Обработка операции перевода"""
    target = input("Введите номер целевого счета: ")
    amount = input_float("Введите сумму перевода: ")
    client.transfer_to_account(target, amount)


def show_client_info(client):
    """Отображение информации о клиенте"""
    print("\n=== ИНФОРМАЦИЯ О КЛИЕНТЕ ===")
    print(client)


def show_client_menu(client, admin):
    """Меню операций с клиентом"""
    menu_options = {
        '1': handle_payment,
        '2': handle_transfer,
        '3': lambda c: c.block_credit_card(),
        '5': show_client_info
    }

    while True:
        print("\n=== ОПЕРАЦИИ С КЛИЕНТЕМ ===")
        print("1. Оплатить заказ")
        print("2. Перевести на другой счет")
        print("3. Блокировать кредитную карту")
        print("4. Аннулировать счет")
        print("5. Показать информацию")
        print("6. Вернуться в меню")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == '4':
            confirm = input("Вы уверены? Счет будет аннулирован! (y/n): ").lower() == 'y'
            if confirm:
                client.close_account()
                return
        elif choice == '6':
            return
        elif choice == '7':
            print("\nВыход из системы...")
            sys.exit()
        elif choice in menu_options:
            menu_options[choice](client)
        else:
            print("Неверный выбор!")

        admin.block_card_for_excess(client)


def show_admin_menu(clients):
    """Меню администратора"""
    admin = Administrator()
    print("\n=== АДМИНИСТРАТИВНЫЕ ФУНКЦИИ ===")
    for i, client in enumerate(clients, 1):
        print(f"{i}. {client.name}")

    try:
        selected = int(input("Выберите клиента для проверки (номер): ")) - 1
        if 0 <= selected < len(clients):
            if admin.block_card_for_excess(clients[selected]):
                print(f"Карта клиента {clients[selected].name} была заблокирована!")
            else:
                print(f"Кредитный лимит клиента {clients[selected].name} не превышен")
        else:
            print("Неверный номер клиента!")
    except ValueError:
        print("Пожалуйста, введите число!")


def main():
    """Главная функция программы"""
    print("\n=== БАНКОВСКАЯ СИСТЕМА 'ПЛАТЕЖИ' ===")
    clients = []
    admin = Administrator()

    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Создать нового клиента")
        print("2. Выбрать клиента")
        print("3. Административные функции")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            clients.append(create_client())
            print("\nКлиент успешно создан!")
            print(clients[-1])
        elif choice == '2':
            if not clients:
                print("Нет зарегистрированных клиентов!")
                continue
            
            print("\nСписок клиентов:")
            for i, client in enumerate(clients, 1):
                print(f"{i}. {client.name}")
            
            try:
                selected = int(input("Выберите клиента (номер): ")) - 1
                if 0 <= selected < len(clients):
                    show_client_menu(clients[selected], admin)
                else:
                    print("Неверный номер клиента!")
            except ValueError:
                print("Пожалуйста, введите число!")
        elif choice == '3':
            if not clients:
                print("Нет зарегистрированных клиентов!")
                continue
            show_admin_menu(clients)
        elif choice == '4':
            print("\nВыход из системы...")
            sys.exit()


if __name__ == "__main__":
    main()

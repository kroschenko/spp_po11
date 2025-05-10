import sys

class Subscriber:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.services = []
        self.is_active = True
        self.balance = 0.0

    def pay_bill(self, amount):
        if amount <= 0:
            print("Ошибка: Сумма платежа должна быть положительной.")
            return
        self.balance += amount
        print(f"Абонент {self.name} пополнил баланс на {amount}. Текущий баланс: {self.balance}")

    def request_service_change(self, admin, new_services):
        if not self.is_active:
            print(f"Ошибка: Абонент {self.name} временно отключен.")
            return
        admin.change_services(self, new_services)

    def request_number_change(self, admin, new_number):
        if not self.is_active:
            print(f"Ошибка: Абонент {self.name} временно отключен.")
            return
        admin.change_number(self, new_number)

    def __str__(self):
        status = "Активен" if self.is_active else "Отключен"
        return f"Абонент: {self.name}, Номер: {self.phone_number}, Баланс: {self.balance}, Статус: {status}"


class Admin:
    def change_number(self, subscriber, new_number):
        subscriber.phone_number = new_number
        print(f"Администратор изменил номер абонента {subscriber.name} на {new_number}")

    def change_services(self, subscriber, new_services):
        subscriber.services = new_services
        print(f"Администратор обновил услуги абонента {subscriber.name}: {', '.join(new_services)}")

    def suspend_subscriber(self, subscriber):
        subscriber.is_active = False
        print(f"Администратор временно отключил абонента {subscriber.name}")


class PhoneStation:
    def __init__(self):
        self.subscribers = {}

    def add_subscriber(self, name, phone_number):
        if name in self.subscribers:
            print(f"Ошибка: Абонент с именем '{name}' уже существует.")
            return
        self.subscribers[name] = Subscriber(name, phone_number)
        print(f"Абонент '{name}' успешно добавлен.")

    def process_payment(self, name, amount):
        if name not in self.subscribers:
            print(f"Ошибка: Абонент '{name}' не найден.")
            return
        self.subscribers[name].pay_bill(amount)

    def request_service_change(self, name, admin, new_services):
        if name not in self.subscribers:
            print(f"Ошибка: Абонент '{name}' не найден.")
            return
        self.subscribers[name].request_service_change(admin, new_services)

    def request_number_change(self, name, admin, new_number):
        if name not in self.subscribers:
            print(f"Ошибка: Абонент '{name}' не найден.")
            return
        self.subscribers[name].request_number_change(admin, new_number)

    def suspend_subscriber(self, name, admin):
        if name not in self.subscribers:
            print(f"Ошибка: Абонент '{name}' не найден.")
            return
        admin.suspend_subscriber(self.subscribers[name])

    def show_info(self):
        print("\nСписок абонентов:")
        for subscriber in self.subscribers.values():
            print(subscriber)


def main():
    print("Добро пожаловать в систему телефонной станции!")
    station = PhoneStation()
    admin = Admin()

    actions = {
        "1": lambda: station.add_subscriber(
            input("Введите имя абонента: "),
            input("Введите номер телефона: ")
        ),
        "2": lambda: station.process_payment(
            input("Введите имя абонента: "),
            float(input("Введите сумму платежа: "))
        ),
        "3": lambda: station.request_service_change(
            input("Введите имя абонента: "),
            admin,
            input("Введите новые услуги через запятую: ").split(",")
        ),
        "4": lambda: station.request_number_change(
            input("Введите имя абонента: "),
            admin,
            input("Введите новый номер телефона: ")
        ),
        "5": lambda: station.suspend_subscriber(
            input("Введите имя абонента: "),
            admin
        ),
        "6": lambda: station.show_info(),
        "7": lambda: sys.exit("Программа завершена."),
    }

    while True:
        print("""
Выберите действие:
1. Добавить абонента
2. Оплатить счет
3. Изменить услуги
4. Изменить номер
5. Отключить абонента
6. Вывести информацию об абонентах
7. Выход
""")
        choice = input("Введите номер действия: ")
        action = actions.get(choice, lambda: print("Некорректный выбор. Попробуйте снова."))
        action()

if __name__ == "__main__":
    main()

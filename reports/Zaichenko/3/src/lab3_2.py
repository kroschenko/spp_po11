from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def get_features(self):
        pass

    @abstractmethod
    def get_discount(self):
        pass


class BasicAccount(Account):
    def get_features(self):
        return ["Доступ к обычным книгам", "Базовая поддержка"]

    def get_discount(self):
        return 0


class AccountDecorator(Account):
    def __init__(self, wrapped_account: Account):
        self._wrapped_account = wrapped_account


class PremiumAccount(AccountDecorator):
    def get_features(self):
        return self._wrapped_account.get_features() + [
            "Бесплатная доставка", "Доступ к премиум-акциям"
        ]

    def get_discount(self):
        return self._wrapped_account.get_discount() + 5


class VIPAccount(AccountDecorator):
    def get_features(self):
        return self._wrapped_account.get_features() + [
            "Личный менеджер", "Эксклюзивные издания"
        ]

    def get_discount(self):
        return self._wrapped_account.get_discount() + 10


def user_interface():
    name = input("Введите ваше имя: ")
    account: Account = BasicAccount()

    print(f"\nПривет, {name}! Ваша базовая учётная запись активирована.")

    while True:
        print("\nВыберите действие:")
        print("1 — Добавить уровень Premium")
        print("2 — Добавить уровень VIP")
        print("3 — Показать текущие функции и скидку")
        print("0 — Выйти")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            account = PremiumAccount(account)
            print("Уровень Premium добавлен.")
        elif choice == "2":
            account = VIPAccount(account)
            print("Уровень VIP добавлен.")
        elif choice == "3":
            print(f"\n{name}, ваши функции:")
            for feature in account.get_features():
                print(" -", feature)
            print(f"Ваша общая скидка: {account.get_discount()}%")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    user_interface()
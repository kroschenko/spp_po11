from abc import ABC, abstractmethod

# Базовый класс для всех уровней учетной записи
class AccountLevel(ABC):
    def __init__(self):
        self.next_level = None

    def set_next(self, next_level):
        self.next_level = next_level
        return next_level

    @abstractmethod
    def handle_request(self, user_activity):
        pass

# Уровень 1: Начальный уровень (Newbie)
class NewbieLevel(AccountLevel):
    def handle_request(self, user_activity):
        if user_activity < 10:
            print("Вы находитесь на уровне Newbie. Доступны базовые функции.")
        elif self.next_level:
            self.next_level.handle_request(user_activity)

# Уровень 2: Продвинутый уровень (Advanced)
class AdvancedLevel(AccountLevel):
    def handle_request(self, user_activity):
        if 10 <= user_activity < 50:
            print("Вы находитесь на уровне Advanced. Доступны скидки до 10%.")
        elif self.next_level:
            self.next_level.handle_request(user_activity)

# Уровень 3: Экспертный уровень (Expert)
class ExpertLevel(AccountLevel):
    def handle_request(self, user_activity):
        if 50 <= user_activity < 100:
            print("Вы находитесь на уровне Expert. Доступны скидки до 25% и эксклюзивные предложения.")
        elif self.next_level:
            self.next_level.handle_request(user_activity)

# Уровень 4: VIP уровень (VIP)
class VIPLevel(AccountLevel):
    def handle_request(self, user_activity):
        if user_activity >= 100:
            print("Вы находитесь на уровне VIP. Доступны скидки до 50%, персональные предложения и приоритетная поддержка.")
        else:
            print("Ошибка: Уровень учетной записи не определен.")

# Класс для управления учетной записью пользователя
class UserAccount:
    def __init__(self, name):
        self.name = name
        self.user_activity = 0  # Активность пользователя (например, количество заказов)
        self.purchase_history = []  # История покупок
        self.free_books = []  # Бесплатные книги, выбранные после получения VIP-статуса
        self.is_vip = False  # Флаг для отслеживания VIP-статуса

    def add_purchase(self, book_name, book_price):
        """Добавляет покупку книги и начисляет очки активности."""
        activity_points = int(book_price)  # Очки активности равны стоимости книги
        self.user_activity += activity_points
        self.purchase_history.append((book_name, book_price))
        print(f"Книга '{book_name}' стоимостью {book_price} добавлена в историю покупок.")
        print(f"Начислено {activity_points} очков активности. Общая активность: {self.user_activity}")

    def check_account_level(self):
        # Создаем цепочку уровней
        newbie_level = NewbieLevel()
        advanced_level = AdvancedLevel()
        expert_level = ExpertLevel()
        vip_level = VIPLevel()

        # Устанавливаем порядок обработки
        newbie_level.set_next(advanced_level).set_next(expert_level).set_next(vip_level)

        # Проверяем уровень учетной записи
        print(f"\nПроверка уровня учетной записи для пользователя {self.name}:")
        newbie_level.handle_request(self.user_activity)

        # Если достигнут VIP-уровень, предлагаем выбрать бесплатные книги
        if self.user_activity >= 100 and not self.is_vip:
            self.is_vip = True
            self.choose_free_books()

    def choose_free_books(self):
        """Предлагает пользователю выбрать бесплатные книги после получения VIP-статуса."""
        print("\nПоздравляем! Вы получили VIP-статус!")
        print("Выберите до 3 бесплатных книг из списка:")

        free_book_options = [
            "1. 'Мастер и Маргарита' - Михаил Булгаков",
            "2. '1984' - Джордж Оруэлл",
            "3. 'Убить пересмешника' - Харпер Ли",
            "4. 'Великий Гэтсби' - Фрэнсис Скотт Фицджеральд",
            "5. 'Гордость и предубеждение' - Джейн Остин"
        ]

        for option in free_book_options:
            print(option)

        while len(self.free_books) < 3:
            choice = input(f"Выберите книгу (введите номер от 1 до {len(free_book_options)}): ")
            if choice.isdigit() and 1 <= int(choice) <= len(free_book_options):
                selected_book = free_book_options[int(choice) - 1]
                if selected_book not in self.free_books:
                    self.free_books.append(selected_book)
                    print(f"Книга '{selected_book}' добавлена в вашу коллекцию.")
                else:
                    print("Эта книга уже выбрана. Пожалуйста, выберите другую.")
            else:
                print("Неверный выбор. Пожалуйста, введите корректный номер.")

            if len(self.free_books) < 3:
                continue_choice = input("Хотите выбрать еще одну книгу? (да/нет): ").lower()
                if continue_choice != "да":
                    break

        print("\nВаши бесплатные книги:")
        for book in self.free_books:
            print(f"- {book}")

    def show_purchase_history(self):
        """Выводит историю покупок пользователя."""
        if not self.purchase_history:
            print("История покупок пуста.")
            return

        print("\nИстория покупок:")
        for i, (book_name, book_price) in enumerate(self.purchase_history, start=1):
            print(f"{i}. Книга: {book_name}, Стоимость: {book_price}")

# Пример использования
if __name__ == "__main__":
    # Создаем учетную запись пользователя
    user = UserAccount("JohnDoe")

    while True:
        print("\nМеню:")
        print("1. Добавить покупку книги")
        print("2. Проверить уровень учетной записи")
        print("3. Показать историю покупок")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            book_name = input("Введите название книги: ")
            book_price = input("Введите стоимость книги: ")
            if book_price.isdigit():
                user.add_purchase(book_name, int(book_price))
            else:
                print("Ошибка: Стоимость книги должна быть числом.")
        elif choice == "2":
            user.check_account_level()
        elif choice == "3":
            user.show_purchase_history()
        elif choice == "4":
            print("Спасибо за использование системы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")
            
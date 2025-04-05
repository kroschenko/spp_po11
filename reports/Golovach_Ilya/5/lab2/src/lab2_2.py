from datetime import datetime

# Базовый класс для всех людей
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


# Класс Читатель
class Reader(Person):
    def __init__(self, name):
        super().__init__(name)
        self.orders = []  # Список заказов читателя
        self.is_blacklisted = False  # Флаг "черного списка"

    def place_order(self, book, catalog):
        """Оформить заказ на книгу."""
        if self.is_blacklisted:
            print(f"Ошибка: Читатель {self.name} находится в черном списке. Заказ невозможен.")
            return None

        order = Order(book, self)
        if catalog.search_book(book):
            self.orders.append(order)
            print(f"Читатель {self.name} оформил заказ на книгу '{book.title}'.")
            return order
        else:
            print(f"Ошибка: Книга '{book.title}' отсутствует в каталоге.")
            return None

    def return_book(self, order):
        """Вернуть книгу."""
        if order in self.orders:
            self.orders.remove(order)
            order.return_book()
            print(f"Читатель {self.name} вернул книгу '{order.book.title}'.")
        else:
            print(f"Ошибка: У читателя {self.name} нет заказа на книгу '{order.book.title}'.")

    def blacklist(self):
        """Добавить читателя в черный список."""
        self.is_blacklisted = True
        print(f"Читатель {self.name} добавлен в черный список.")


# Класс Книга
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Класс Заказ
class Order:
    def __init__(self, book, reader):
        self.book = book
        self.reader = reader
        self.issue_date = datetime.now()
        self.return_date = None

    def return_book(self):
        """Пометить книгу как возвращенную."""
        self.return_date = datetime.now()
        print(f"Книга '{self.book.title}' возвращена читателем {self.reader.name}.")


# Класс Каталог
class Catalog:
    def __init__(self):
        self.books = []  # Список книг в каталоге

    def add_book(self, book):
        """Добавить книгу в каталог."""
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в каталог.")

    def search_book(self, book):
        """Поиск книги в каталоге."""
        return book in self.books


# Класс Библиотекарь
class Librarian(Person):
    def issue_book(self, order):
        """Выдать книгу читателю."""
        print(f"Библиотекарь {self.name} выдал книгу '{order.book.title}' читателю {order.reader.name}.")


# Интерфейс для управления
class IManageable:
    def manage_blacklist(self, reader):
        pass


# Класс Администратор
class Administrator(Person, IManageable):
    def __init__(self, name):
        super().__init__(name)
        self.blacklist = []

    def manage_blacklist(self, reader):
        """Добавить читателя в черный список."""
        if not reader.is_blacklisted:
            reader.blacklist()
            self.blacklist.append(reader)
            print(f"Администратор {self.name} добавил читателя {reader.name} в черный список.")
        else:
            print(f"Ошибка: Читатель {reader.name} уже находится в черном списке.")


# Вспомогательная функция для безопасного ввода данных
def safe_input(prompt, error_message="Некорректный ввод. Попробуйте снова.", validator=lambda x: x):
    while True:
        try:
            value = input(prompt)
            if validator(value):
                return value
            else:
                print(error_message)
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте снова.")


# Основная программа
def main():
    print("Добро пожаловать в систему библиотеки!")

    # Создание объектов
    librarian = Librarian("Мария Петровна")
    admin = Administrator("Александр Сидоров")
    catalog = Catalog()

    readers = {}
    books = {}

    while True:
        print("\nВыберите действие:")
        print("1. Добавить читателя")
        print("2. Добавить книгу в каталог")
        print("3. Оформить заказ на книгу")
        print("4. Вернуть книгу")
        print("5. Добавить читателя в черный список")
        print("6. Вывести информацию о читателях и книгах")
        print("7. Выход")

        choice = safe_input(
            "Введите номер действия: ",
            error_message="Ошибка: Введите число от 1 до 7.",
            validator=lambda x: x.isdigit() and 1 <= int(x) <= 7
        )

        if choice == "1":
            try:
                name = safe_input("Введите имя читателя: ")
                if name in readers:
                    print(f"Ошибка: Читатель с именем '{name}' уже существует.")
                else:
                    readers[name] = Reader(name)
                    print(f"Читатель '{name}' успешно добавлен.")
            except Exception as e:
                print(f"Ошибка при добавлении читателя: {e}")

        elif choice == "2":
            try:
                title = safe_input("Введите название книги: ")
                author = safe_input("Введите автора книги: ")
                book = Book(title, author)
                catalog.add_book(book)
                books[title] = book
                print(f"Книга '{title}' успешно добавлена в каталог.")
            except Exception as e:
                print(f"Ошибка при добавлении книги: {e}")

        elif choice == "3":
            try:
                reader_name = safe_input("Введите имя читателя: ")
                if reader_name not in readers:
                    print(f"Ошибка: Читатель с именем '{reader_name}' не найден.")
                    continue

                book_title = safe_input("Введите название книги: ")
                if book_title not in books:
                    print(f"Ошибка: Книга с названием '{book_title}' не найдена.")
                    continue

                reader = readers[reader_name]
                book = books[book_title]
                order = reader.place_order(book, catalog)
                if order:
                    librarian.issue_book(order)
            except Exception as e:
                print(f"Ошибка при оформлении заказа: {e}")

        elif choice == "4":
            try:
                reader_name = safe_input("Введите имя читателя: ")
                if reader_name not in readers:
                    print(f"Ошибка: Читатель с именем '{reader_name}' не найден.")
                    continue

                book_title = safe_input("Введите название книги: ")
                if book_title not in books:
                    print(f"Ошибка: Книга с названием '{book_title}' не найдена.")
                    continue

                reader = readers[reader_name]
                book = books[book_title]
                for order in reader.orders:
                    if order.book == book:
                        reader.return_book(order)
                        break
                else:
                    print(f"Ошибка: У читателя '{reader_name}' нет заказа на книгу '{book_title}'.")
            except Exception as e:
                print(f"Ошибка при возврате книги: {e}")

        elif choice == "5":
            try:
                reader_name = safe_input("Введите имя читателя: ")
                if reader_name not in readers:
                    print(f"Ошибка: Читатель с именем '{reader_name}' не найден.")
                    continue

                reader = readers[reader_name]
                admin.manage_blacklist(reader)
            except Exception as e:
                print(f"Ошибка при добавлении в черный список: {e}")

        elif choice == "6":
            try:
                print("\nСписок читателей:")
                for name, reader in readers.items():
                    status = " (в черном списке)" if reader.is_blacklisted else ""
                    print(f"- {name}{status}")

                print("\nСписок книг в каталоге:")
                for title, book in books.items():
                    print(f"- {book}")
            except Exception as e:
                print(f"Ошибка при выводе информации: {e}")

        elif choice == "7":
            print("Программа завершена.")
            break


if __name__ == "__main__":
    main()
from datetime import datetime


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Reader(Person):
    def __init__(self, name):
        super().__init__(name)
        self.orders = []
        self.is_blacklisted = False

    def place_order(self, book, catalog):
        if self.is_blacklisted:
            print(f"Ошибка: Читатель {self.name} находится в черном списке. Заказ невозможен.")
            return None

        if not catalog.search_book(book):
            print(f"Ошибка: Книга '{book.title}' отсутствует в каталоге.")
            return None

        order = Order(book, self)
        self.orders.append(order)
        print(f"Читатель {self.name} оформил заказ на книгу '{book.title}'.")
        return order

    def return_book(self, order):
        if order not in self.orders:
            print(f"Ошибка: У читателя {self.name} нет заказа на книгу '{order.book.title}'.")
            return

        self.orders.remove(order)
        order.return_book()
        print(f"Читатель {self.name} вернул книгу '{order.book.title}'.")

    def blacklist(self):
        self.is_blacklisted = True
        print(f"Читатель {self.name} добавлен в черный список.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Order:
    def __init__(self, book, reader):
        self.book = book
        self.reader = reader
        self.issue_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()
        print(f"Книга '{self.book.title}' возвращена читателем {self.reader.name}.")


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в каталог.")

    def search_book(self, book):
        return book in self.books


class Librarian(Person):
    def issue_book(self, order):
        print(f"Библиотекарь {self.name} выдал книгу '{order.book.title}' читателю {order.reader.name}.")


class IManageable:
    def manage_blacklist(self, reader):
        pass


class Administrator(Person, IManageable):
    def __init__(self, name):
        super().__init__(name)
        self.blacklist = []

    def manage_blacklist(self, reader):
        if reader.is_blacklisted:
            print(f"Ошибка: Читатель {reader.name} уже находится в черном списке.")
            return

        reader.blacklist()
        self.blacklist.append(reader)
        print(f"Администратор {self.name} добавил читателя {reader.name} в черный список.")


def safe_input(prompt, error_message="Некорректный ввод. Попробуйте снова.", validator=lambda x: x):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_message)


def get_reader(readers):
    name = safe_input("Введите имя читателя: ")
    if name not in readers:
        print(f"Ошибка: Читатель с именем '{name}' не найден.")
        return None
    return readers[name]


def get_book(books):
    title = safe_input("Введите название книги: ")
    if title not in books:
        print(f"Ошибка: Книга с названием '{title}' не найдена.")
        return None
    return books[title]


def add_reader(readers):
    name = safe_input("Введите имя читателя: ")
    if name in readers:
        print(f"Ошибка: Читатель с именем '{name}' уже существует.")
        return readers
    readers[name] = Reader(name)
    print(f"Читатель '{name}' успешно добавлен.")
    return readers


def add_book(catalog, books):
    title = safe_input("Введите название книги: ")
    author = safe_input("Введите автора книги: ")
    book = Book(title, author)
    catalog.add_book(book)
    books[title] = book
    print(f"Книга '{title}' успешно добавлена в каталог.")
    return books


def place_order(readers, books, catalog, librarian):
    reader = get_reader(readers)
    if not reader:
        return

    book = get_book(books)
    if not book:
        return

    order = reader.place_order(book, catalog)
    if order:
        librarian.issue_book(order)


def return_book(readers, books):
    reader = get_reader(readers)
    if not reader:
        return

    book = get_book(books)
    if not book:
        return

    for order in reader.orders:
        if order.book == book:
            reader.return_book(order)
            break
    else:
        print(f"Ошибка: У читателя '{reader.name}' нет заказа на книгу '{book.title}'.")


def manage_blacklist(readers, admin):
    reader = get_reader(readers)
    if reader:
        admin.manage_blacklist(reader)


def show_info(readers, books):
    print("\nСписок читателей:")
    for name, reader in readers.items():
        status = " (в черном списке)" if reader.is_blacklisted else ""
        print(f"- {name}{status}")

    print("\nСписок книг в каталоге:")
    for book in books.values():
        print(f"- {book}")


def main():
    print("Добро пожаловать в систему библиотеки!")
    librarian = Librarian("Мария Петровна")
    admin = Administrator("Александр Сидоров")
    catalog = Catalog()
    readers = {}
    books = {}

    actions = {
        "1": lambda: add_reader(readers),
        "2": lambda: add_book(catalog, books),
        "3": lambda: place_order(readers, books, catalog, librarian),
        "4": lambda: return_book(readers, books),
        "5": lambda: manage_blacklist(readers, admin),
        "6": lambda: show_info(readers, books),
        "7": lambda: exit(print("Программа завершена.")),
    }

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
            validator=lambda x: x.isdigit() and 1 <= int(x) <= 7,
        )

        action = actions.get(choice, lambda: print("Некорректный выбор. Попробуйте снова."))
        action()


if __name__ == "__main__":
    main()

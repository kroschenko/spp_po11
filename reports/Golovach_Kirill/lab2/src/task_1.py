class LimitedRealSet:
    def __init__(self, max_size, initial_elements=None):
        if initial_elements is None:
            initial_elements = []
        if len(initial_elements) > max_size:
            raise ValueError("Количество начальных элементов превышает максимальную мощность множества")
        self.max_size = max_size
        self.elements = list(set(initial_elements))  # Уникальные элементы

    def add(self, value):
        if value in self.elements:
            print(f"Элемент {value} уже существует в множестве")
            return False
        if len(self.elements) >= self.max_size:
            print("Множество достигло максимальной мощности. Элемент не может быть добавлен")
            return False
        self.elements.append(value)
        print(f"Элемент {value} добавлен успешно")
        return True

    def remove(self, value):
        if value not in self.elements:
            print(f"Элемент {value} не найден в множестве")
            return False
        self.elements.remove(value)
        print(f"Элемент {value} удалён успешно")
        return True

    def intersection(self, other_set):
        if not isinstance(other_set, LimitedRealSet):
            raise TypeError("Пересечение возможно только с объектами типа LimitedRealSet")
        common_elements = list(set(self.elements).intersection(other_set.elements))
        return LimitedRealSet(max(self.max_size, other_set.max_size), common_elements)

    def contains(self, value):
        return value in self.elements

    def __str__(self):
        return f"Множество: {self.elements}, Максимальная мощность: {self.max_size}"

    def __eq__(self, other):
        if not isinstance(other, LimitedRealSet):
            return False
        return set(self.elements) == set(other.elements)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите вещественное число.")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")


def create_set(set_number):
    max_size = get_integer(f"Введите максимальную мощность {set_number} множества: ")
    initial_elements = input(
        f"Введите начальные элементы {set_number} множества через пробел (или оставьте пустым): "
    ).split()
    initial_elements = [float(x) for x in initial_elements] if initial_elements else []
    return LimitedRealSet(max_size, initial_elements)


def add_element(set1, set2):
    set_num = input("В какое множество добавить элемент? (1 или 2): ")
    value = get_float("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        target_set.add(value)
    else:
        print("Некорректный выбор множества.")


def remove_element(set1, set2):
    set_num = input("Из какого множества удалить элемент? (1 или 2): ")
    value = get_float("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        target_set.remove(value)
    else:
        print("Некорректный выбор множества.")


def check_element(set1, set2):
    set_num = input("В каком множестве проверить принадлежность? (1 или 2): ")
    value = get_float("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        print(f"Элемент {value} {'принадлежит' if target_set.contains(value) else 'не принадлежит'} множеству.")
    else:
        print("Некорректный выбор множества.")


def intersect_sets(set1, set2):
    result = set1.intersection(set2)
    print(f"Результат пересечения множеств: {result}")


def compare_sets(set1, set2):
    print("Множества равны." if set1 == set2 else "Множества не равны.")


def show_sets(set1, set2):
    print(f"Первое множество: {set1}")
    print(f"Второе множество: {set2}")


def handle_set_operation(choice, set1, set2):
    actions = {
        "1": lambda: add_element(set1, set2),
        "2": lambda: remove_element(set1, set2),
        "3": lambda: check_element(set1, set2),
        "4": lambda: intersect_sets(set1, set2),
        "5": lambda: compare_sets(set1, set2),
        "6": lambda: show_sets(set1, set2),
    }
    action = actions.get(choice, lambda: print("Некорректный выбор. Попробуйте снова."))
    action()


def print_menu():
    print("""
Выберите действие:
1. Добавить элемент в множество
2. Удалить элемент из множества
3. Проверить принадлежность элемента множеству
4. Пересечь множества
5. Сравнить множества
6. Вывести информацию о множествах
7. Выход
""")


def main():
    print("Добро пожаловать в программу для работы с множествами вещественных чисел ограниченной мощности!")
    try:
        set1 = create_set("первого")
        print(f"Создано первое множество: {set1}\n")
        set2 = create_set("второго")
        print(f"Создано второе множество: {set2}\n")
    except ValueError as e:
        print(f"Ошибка при создании множества: {e}")
        return
    while True:
        print_menu()
        choice = input("Введите номер действия: ")
        if choice == "7":
            print("Программа завершена.")
            break
        handle_set_operation(choice, set1, set2)


if __name__ == "__main__":
    main()

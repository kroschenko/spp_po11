class LimitedPowerSet:
    def __init__(self, max_size, initial_elements=None):
        if initial_elements is None:
            initial_elements = []

        if len(initial_elements) > max_size:
            raise ValueError("Количество начальных элементов превышает максимальную мощность множества")

        self.max_size = max_size
        self.elements = list(set(initial_elements))

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

    def union(self, other_set):
        if not isinstance(other_set, LimitedPowerSet):
            raise TypeError("Объединение возможно только с объектами типа LimitedPowerSet")

        new_max_size = self.max_size + other_set.max_size
        new_elements = list(set(self.elements).union(other_set.elements))
        return LimitedPowerSet(new_max_size, new_elements)

    def contains(self, value):
        return value in self.elements

    def __str__(self):
        return f"Множество: {self.elements}, Максимальная мощность: {self.max_size}"

    def __eq__(self, other):
        if not isinstance(other, LimitedPowerSet):
            return False
        return set(self.elements) == set(other.elements)


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
    initial_elements = [int(x) for x in initial_elements] if initial_elements else []
    return LimitedPowerSet(max_size, initial_elements)


def add_element(set1, set2):
    set_num = input("В какое множество добавить элемент? (1 или 2): ")
    value = get_integer("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        target_set.add(value)
    else:
        print("Некорректный выбор множества.")


def remove_element(set1, set2):
    set_num = input("Из какого множества удалить элемент? (1 или 2): ")
    value = get_integer("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        target_set.remove(value)
    else:
        print("Некорректный выбор множества.")


def check_element(set1, set2):
    set_num = input("В каком множестве проверить принадлежность? (1 или 2): ")
    value = get_integer("Введите значение элемента: ")
    target_set = set1 if set_num == "1" else set2 if set_num == "2" else None
    if target_set:
        print(f"Элемент {value} {'принадлежит' if target_set.contains(value) else 'не принадлежит'} множеству.")
    else:
        print("Некорректный выбор множества.")


def union_sets(set1, set2):
    result = set1.union(set2)
    print(f"Результат объединения множеств: {result}")


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
        "4": lambda: union_sets(set1, set2),
        "5": lambda: compare_sets(set1, set2),
        "6": lambda: show_sets(set1, set2),
    }
    action = actions.get(choice, lambda: print("Некорректный выбор. Попробуйте снова."))
    action()


def print_menu():
    print("\nВыберите действие:")
    print("1. Добавить элемент в множество")
    print("2. Удалить элемент из множества")
    print("3. Проверить принадлежность элемента множеству")
    print("4. Объединить множества")
    print("5. Сравнить множества")
    print("6. Вывести информацию о множествах")
    print("7. Выход")


def main():
    print("Добро пожаловать в программу для работы с множествами ограниченной мощности!")

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

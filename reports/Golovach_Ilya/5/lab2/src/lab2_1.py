class LimitedPowerSet:
    def __init__(self, max_size, initial_elements=None):
        if initial_elements is None:
            initial_elements = []

        try:
            if len(initial_elements) > max_size:
                raise ValueError("Количество начальных элементов превышает максимальную мощность множества")
        except ValueError as e:
            print(f"Ошибка: {e}")
            raise  # Перебрасываем исключение, чтобы программа могла корректно обработать его на уровне main()

        self.max_size = max_size
        self.elements = list(set(initial_elements))

    def add(self, value):
        try:
            if value in self.elements:
                print(f"Элемент {value} уже существует в множестве")
                return

            if len(self.elements) >= self.max_size:
                print(f"Множество достигло максимальной мощности. Элемент не может быть добавлен")
                return

            self.elements.append(value)
            print(f"Элемент {value} добавлен успешно")
        except Exception as e:
            print(f"Ошибка при добавлении элемента: {e}")

    def remove(self, value):
        try:
            if value in self.elements:
                self.elements.remove(value)
                print(f"Элемент {value} удалён успешно")
            else:
                print(f"Элемент {value} не найден в множестве")
        except Exception as e:
            print(f"Ошибка при удалении элемента: {e}")

    def union(self, other_set):
        try:
            if not isinstance(other_set, LimitedPowerSet):
                raise TypeError("Объединение возможно только с объектами типа LimitedPowerSet")

            new_max_size = self.max_size + other_set.max_size
            new_elements = list(set(self.elements).union(other_set.elements))
            return LimitedPowerSet(new_max_size, new_elements)
        except Exception as e:
            print(f"Ошибка при объединении множеств: {e}")
            return None

    def contains(self, value):
        try:
            return value in self.elements
        except Exception as e:
            print(f"Ошибка при проверке принадлежности элемента: {e}")
            return False

    def __str__(self):
        try:
            return f"Множество: {self.elements}, Максимальная мощность: {self.max_size}"
        except Exception as e:
            print(f"Ошибка при формировании строкового представления множества: {e}")
            return "Ошибка: Недоступно для отображения"

    def __eq__(self, other):
        try:
            if not isinstance(other, LimitedPowerSet):
                return False
            return set(self.elements) == set(other.elements)
        except Exception as e:
            print(f"Ошибка при сравнении множеств: {e}")
            return False


def get_integer(prompt):
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Ошибка: Введите целое число.")


def main():
    print("Добро пожаловать в программу для работы с множествами ограниченной мощности!")

    try:
        max_size1 = get_integer("Введите максимальную мощность первого множества: ")
        initial_elements1 = input(
            "Введите начальные элементы первого множества через пробел (или оставьте пустым): ").split()
        initial_elements1 = [int(x) for x in initial_elements1] if initial_elements1 else []
        set1 = LimitedPowerSet(max_size1, initial_elements1)
        print(f"Создано первое множество: {set1}\n")
    except Exception as e:
        print(f"Ошибка при создании первого множества: {e}")
        return

    try:
        max_size2 = get_integer("Введите максимальную мощность второго множества: ")
        initial_elements2 = input(
            "Введите начальные элементы второго множества через пробел (или оставьте пустым): ").split()
        initial_elements2 = [int(x) for x in initial_elements2] if initial_elements2 else []
        set2 = LimitedPowerSet(max_size2, initial_elements2)
        print(f"Создано второе множество: {set2}\n")
    except Exception as e:
        print(f"Ошибка при создании второго множества: {e}")
        return

    while True:
        try:
            print("\nВыберите действие:")
            print("1. Добавить элемент в множество")
            print("2. Удалить элемент из множества")
            print("3. Проверить принадлежность элемента множеству")
            print("4. Объединить множества")
            print("5. Сравнить множества")
            print("6. Вывести информацию о множествах")
            print("7. Выход")

            choice = input("Введите номер действия: ")

            if choice == "1":
                try:
                    set_num = input("В какое множество добавить элемент? (1 или 2): ")
                    value = get_integer("Введите значение элемента: ")
                    if set_num == "1":
                        set1.add(value)
                    elif set_num == "2":
                        set2.add(value)
                    else:
                        print("Некорректный выбор множества.")
                except Exception as e:
                    print(f"Ошибка при добавлении элемента: {e}")

            elif choice == "2":
                try:
                    set_num = input("Из какого множества удалить элемент? (1 или 2): ")
                    value = get_integer("Введите значение элемента: ")
                    if set_num == "1":
                        set1.remove(value)
                    elif set_num == "2":
                        set2.remove(value)
                    else:
                        print("Некорректный выбор множества.")
                except Exception as e:
                    print(f"Ошибка при удалении элемента: {e}")

            elif choice == "3":
                try:
                    set_num = input("В каком множестве проверить принадлежность? (1 или 2): ")
                    value = get_integer("Введите значение элемента: ")
                    if set_num == "1":
                        result = set1.contains(value)
                    elif set_num == "2":
                        result = set2.contains(value)
                    else:
                        print("Некорректный выбор множества.")
                        continue
                    print(f"Элемент {value} {'принадлежит' if result else 'не принадлежит'} множеству.")
                except Exception as e:
                    print(f"Ошибка при проверке принадлежности: {e}")

            elif choice == "4":
                try:
                    set3 = set1.union(set2)
                    if set3:
                        print(f"Результат объединения множеств: {set3}")
                except Exception as e:
                    print(f"Ошибка при объединении множеств: {e}")

            elif choice == "5":
                try:
                    if set1 == set2:
                        print("Множества равны.")
                    else:
                        print("Множества не равны.")
                except Exception as e:
                    print(f"Ошибка при сравнении множеств: {e}")

            elif choice == "6":
                try:
                    print(f"Первое множество: {set1}")
                    print(f"Второе множество: {set2}")
                except Exception as e:
                    print(f"Ошибка при выводе информации о множествах: {e}")

            elif choice == "7":
                print("Программа завершена.")
                break

            else:
                print("Некорректный выбор. Попробуйте снова.")

        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Продолжаем работу...")


if __name__ == "__main__":
    main()
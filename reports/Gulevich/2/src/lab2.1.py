class LimitedCharSet:
    def __init__(self, capacity, initial_elements=None):
        self.capacity = capacity
        self._elements = []
        if initial_elements:
            for elem in initial_elements:
                self.add(elem)

    def add(self, char):
        if char in self._elements:
            print(f"'{char}' уже есть в множестве.")
        elif len(self._elements) >= self.capacity:
            print(f"Невозможно добавить '{char}': превышена мощность множества.")
        else:
            self._elements.append(char)

    def remove(self, char):
        if char in self._elements:
            self._elements.remove(char)
        else:
            print(f"'{char}' нет в множестве.")

    def contains(self, char):
        return char in self._elements

    def __str__(self):
        return "{" + ", ".join(self._elements) + "}"

    def __eq__(self, other):
        if not isinstance(other, LimitedCharSet):
            return False
        return sorted(self._elements) == sorted(other._elements)

    def union(self, other):
        if not isinstance(other, LimitedCharSet):
            raise TypeError("Можно объединять только с объектом LimitedCharSet")

        new_capacity = max(self.capacity, other.capacity)
        new_set = LimitedCharSet(new_capacity)

        for char in self._elements + other._elements:
            new_set.add(char)

        return new_set

    @property
    def elements(self):
        return list(self._elements)

    @property
    def size(self):
        return len(self._elements)

    @property
    def max_size(self):
        return self.capacity


def main():
    print("== Работа с ограниченным множеством символов ==")
    capacity = int(input("Введите мощность множества: "))
    initial = input("Введите начальные символы (например: abc): ")

    my_set = LimitedCharSet(capacity, list(initial))

    while True:
        print("\nМеню:")
        print("1. Добавить символ")
        print("2. Удалить символ")
        print("3. Проверить наличие символа")
        print("4. Вывести множество")
        print("5. Создать второе множество и объединить")
        print("6. Проверить равенство с другим множеством")
        print("7. Завершить")

        choice = input("Выберите действие: ")

        if choice == "1":
            ch = input("Введите символ для добавления: ")
            my_set.add(ch)

        elif choice == "2":
            ch = input("Введите символ для удаления: ")
            my_set.remove(ch)

        elif choice == "3":
            ch = input("Введите символ для проверки: ")
            print(f"'{ch}' в множестве? ->", my_set.contains(ch))

        elif choice == "4":
            print("Текущее множество:", my_set)

        elif choice == "5":
            print("== Создание второго множества для объединения ==")
            cap2 = int(input("Введите мощность второго множества: "))
            init2 = input("Введите символы второго множества: ")
            other_set = LimitedCharSet(cap2, list(init2))
            combined = my_set.union(other_set)
            print("Результат объединения:", combined)

        elif choice == "6":
            print("== Создание второго множества для сравнения ==")
            cap2 = int(input("Введите мощность второго множества: "))
            init2 = input("Введите символы второго множества: ")
            other_set = LimitedCharSet(cap2, list(init2))
            print("Множества равны?" , my_set == other_set)

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

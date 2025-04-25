"""Module for working with sets of real numbers."""

from typing import List, Optional, Union


class RealNumberSet:
    """A set of real numbers supporting operations like add, remove, union, and comparison."""

    def __init__(self, initial_elements: Optional[Union[List, set]] = None) -> None:
        """Initialize a set with optional initial elements.

        Args:
            initial_elements: An iterable of numbers (int or float) to initialize the set.
                              Non-numeric values are ignored with a warning.
        """
        self.elements: List[float] = []
        if initial_elements is not None:
            for item in initial_elements:
                try:
                    self.add_element(float(item))
                except (ValueError, TypeError):
                    print(f"Пропущен неверный элемент: {item}")

    def add_element(self, element_: Union[int, float]) -> bool:
        """Add an element to the set if it doesn't already exist.

        Args:
            element_: The number to add (int or float).

        Returns:
            bool: True if the element was added, False if it already exists.
        """
        try:
            element_float = float(element_)
            if element_float not in self.elements:
                self.elements.append(element_float)
                return True
            return False
        except (ValueError, TypeError):
            print(f"Ошибка: '{element_}' не является числом.")
            return False

    def remove_element(self, element_: Union[int, float]) -> bool:
        """Remove an element from the set if it exists.

        Args:
            element_: The number to remove (int or float).

        Returns:
            bool: True if the element was removed, False if it was not found.
        """
        try:
            element_float = float(element_)
            if element_float in self.elements:
                self.elements.remove(element_float)
                return True
            return False
        except (ValueError, TypeError):
            print(f"Ошибка: '{element_}' не является числом.")
            return False

    def union(self, other_set: "RealNumberSet") -> "RealNumberSet":
        """Create a new set containing all elements from this set and another.

        Args:
            other_set: Another RealNumberSet to unite with.

        Returns:
            RealNumberSet: A new set with all unique elements.

        Raises:
            ValueError: If other_set is not a RealNumberSet.
        """
        if not isinstance(other_set, RealNumberSet):
            raise ValueError("Аргумент должен быть объектом RealNumberSet")
        result = RealNumberSet(self.elements)
        for elem in other_set.elements:
            result.add_element(elem)
        return result

    def contains(self, element_: Union[int, float]) -> bool:
        """Check if an element exists in the set.

        Args:
            element_: The number to check (int or float).

        Returns:
            bool: True if the element is in the set, False otherwise.
        """
        try:
            return float(element_) in self.elements
        except (ValueError, TypeError):
            return False

    def print_elements(self) -> None:
        """Print the elements of the set in sorted order."""
        print("Множество:", sorted(self.elements))

    def __str__(self) -> str:
        """Return a string representation of the set.

        Returns:
            str: String of sorted elements.
        """
        return f"RealNumberSet({sorted(self.elements)})"

    def __eq__(self, other: object) -> bool:
        """Check if two sets are equal.

        Args:
            other: Another object to compare with.

        Returns:
            bool: True if the sets have the same elements, False otherwise.
        """
        if not isinstance(other, RealNumberSet):
            return False
        return sorted(self.elements) == sorted(other.elements)


def create_set_interactively(set_name: str) -> RealNumberSet:
    """Interactively create a set by prompting for elements.

    Args:
        set_name: Name of the set for user prompts (e.g., 'первого множества').

    Returns:
        RealNumberSet: A new set with user-provided elements.
    """
    elements = []
    print(f"Создание {set_name} (введите числа, 'q' для завершения):")
    while True:
        user_input = input("Элемент: ")
        if user_input.lower() == "q":
            break
        try:
            elements.append(float(user_input))
        except ValueError:
            print("Ошибка: введите вещественное число.")
    return RealNumberSet(elements)


if __name__ == "__main__":
    print("== Задание 1: Работа с множествами ==")

    # Create first set
    set1 = create_set_interactively("первого множества")

    # Create second set
    set2 = create_set_interactively("второго множества")

    # Interactive menu
    while True:
        print("\nВыберите действие:")
        print("1. Вывести множества")
        print("2. Добавить элемент")
        print("3. Удалить элемент")
        print("4. Проверить принадлежность элемента")
        print("5. Объединить множества")
        print("6. Сравнить множества")
        print("7. Выход")
        choice = input("Ваш выбор (1-7): ")

        if choice == "1":
            print("Первое множество:")
            set1.print_elements()
            print("Второе множество:")
            set2.print_elements()

        elif choice == "2":
            print("\nВыберите множество:")
            print("1. Первое множество")
            print("2. Второе множество")
            sub_choice = input("Ваш выбор (1-2): ")
            new_input = input("Введите элемент для добавления: ")
            try:
                element = float(new_input)
                if sub_choice == "1":
                    if set1.add_element(element):
                        print("Элемент добавлен в первое множество.")
                    else:
                        print("Элемент уже есть в первом множестве.")
                elif sub_choice == "2":
                    if set2.add_element(element):
                        print("Элемент добавлен во второе множество.")
                    else:
                        print("Элемент уже есть во втором множестве.")
                else:
                    print("Неверный выбор множества.")
            except ValueError:
                print("Ошибка: введите вещественное число.")

        elif choice == "3":
            print("\nВыберите множество:")
            print("1. Первое множество")
            print("2. Второе множество")
            sub_choice = input("Ваш выбор (1-2): ")
            new_input = input("Введите элемент для удаления: ")
            try:
                element = float(new_input)
                if sub_choice == "1":
                    if set1.remove_element(element):
                        print("Элемент удален из первого множества.")
                    else:
                        print("Элемент не найден в первом множестве.")
                elif sub_choice == "2":
                    if set2.remove_element(element):
                        print("Элемент удален из второго множества.")
                    else:
                        print("Элемент не найден во втором множестве.")
                else:
                    print("Неверный выбор множества.")
            except ValueError:
                print("Ошибка: введите вещественное число.")

        elif choice == "4":
            print("\nВыберите множество:")
            print("1. Первое множество")
            print("2. Второе множество")
            sub_choice = input("Ваш выбор (1-2): ")
            new_input = input("Введите элемент для проверки: ")
            try:
                element = float(new_input)
                if sub_choice == "1":
                    if set1.contains(element):
                        print(f"Элемент {element} принадлежит первому множеству.")
                    else:
                        print(f"Элемент {element} не принадлежит первому множеству.")
                elif sub_choice == "2":
                    if set2.contains(element):
                        print(f"Элемент {element} принадлежит второму множеству.")
                    else:
                        print(f"Элемент {element} не принадлежит второму множеству.")
                else:
                    print("Неверный выбор множества.")
            except ValueError:
                print("Ошибка: введите вещественное число.")

        elif choice == "5":
            union_set = set1.union(set2)
            print("Результат объединения:")
            union_set.print_elements()

        elif choice == "6":
            print("Множества равны" if set1 == set2 else "Множества не равны.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

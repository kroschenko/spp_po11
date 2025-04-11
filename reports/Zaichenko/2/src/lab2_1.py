class SymbolSet:
    def __init__(self, initial_values=None):
        if initial_values is None:
            self._elements = []
        else:
            self._elements = []
            for val in initial_values:
                self.add(val)

    def add(self, value):
        if value not in self._elements:
            self._elements.append(value)

    def remove(self, value):
        if value in self._elements:
            self._elements.remove(value)

    def contains(self, value):
        return value in self._elements

    def intersect(self, other):
        intersection = [val for val in self._elements if val in other._elements]
        return SymbolSet(intersection)

    def __str__(self):
        return "{" + ", ".join(self._elements) + "}"

    def __eq__(self, other):
        if not isinstance(other, SymbolSet):
            return False
        return set(self._elements) == set(other._elements)

    def display(self):
        print("Множество:", self)

    @property
    def elements(self):
        return self._elements.copy()

    @elements.setter
    def elements(self, values):
        self._elements = []
        for val in values:
            self.add(val)


def create_set_from_input():
    elements = input("Введите элементы множества через пробел: ").split()
    symbol_set = SymbolSet(elements)
    return symbol_set


if __name__ == "__main__":
    print("Создадим первое множество:")
    set1 = create_set_from_input()
    set1.display()

    print("\nСоздадим второе множество:")
    set2 = create_set_from_input()
    set2.display()

    intersected = set1.intersect(set2)
    print("\nПересечение множества 1 и множества 2:")
    intersected.display()

    element_to_add = input("\nВведите элемент для добавления в первое множество: ")
    set1.add(element_to_add)
    element_to_remove = input("Введите элемент для удаления из первого множества: ")
    set1.remove(element_to_remove)

    set1.display()

    print("\nСравнение двух множеств:", set1 == set2)

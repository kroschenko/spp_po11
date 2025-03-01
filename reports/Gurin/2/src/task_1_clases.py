import enum


class IntegerSet:
    def __init__(self, initial_elements=None):
        if initial_elements is None:
            self.elements = []
        else:
            self.elements = list(set({x for x in initial_elements if isinstance(x, int)}))

    def size(self):
        return len(self.elements)

    def add(self, element: int) -> None:
        if isinstance(element, int) and element not in self.elements:
            self.elements.append(element)

    def remove(self, element: int) -> None:
        if isinstance(element, int) and element in self.elements:
            self.elements.remove(element)

    def contains(self, element: int) -> bool:
        return isinstance(element, int) and element in self.elements

    def intersection(self, other_set: "IntegerSet") -> "IntegerSet":
        intersection_set = IntegerSet()
        for element in self.elements:
            if element in other_set.elements:
                intersection_set.add(element)
        return intersection_set

    def __str__(self):
        return "{" + ", ".join(map(str, self.elements)) + "}"

    def __eq__(self, other):
        return set(self.elements) == set(other.elements)


class Choice(enum.Enum):
    SHOW_ELEMENTS = 1
    SHOW_INTERSECTIONS = 2
    ADD_ELEMENT = 3
    REMOVE_ELEMENT = 4
    CHECK_ELEMENT = 5
    EXIT = 6


choiceValues = {
    Choice.SHOW_ELEMENTS.value: "Show elements",
    Choice.SHOW_INTERSECTIONS.value: "Show intersections",
    Choice.ADD_ELEMENT.value: "Add element",
    Choice.REMOVE_ELEMENT.value: "Remove element",
    Choice.CHECK_ELEMENT.value: "Check element",
    Choice.EXIT.value: "Exit",
}

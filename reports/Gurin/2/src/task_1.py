from task_1_clases import Choice, IntegerSet, choiceValues


def show_elements_action(local_set_1: IntegerSet, local_set_2: IntegerSet) -> None:
    while True:
        try:
            user_input: int = int(input("Enter the set number: "))
            if user_input == 1:
                print(local_set_1)
            elif user_input == 2:
                print(local_set_2)
            else:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again.")


def show_intersections_action(local_set_1: IntegerSet, local_set_2: IntegerSet) -> None:
    print(local_set_1.intersection(local_set_2))


def add_element_action(local_set_1: IntegerSet, local_set_2: IntegerSet) -> None:
    while True:
        try:
            user_input: int = int(input("Enter the set number: "))
            value: int = int(input("Enter the element value: "))
            if user_input == 1:
                local_set_1.add(value)
            elif user_input == 2:
                local_set_2.add(value)
            else:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again.")


def remove_element_action(local_set_1: IntegerSet, local_set_2: IntegerSet) -> None:
    while True:
        try:
            user_input: int = int(input("Enter the set number: "))
            value: int = int(input("Enter the element value: "))
            if user_input == 1:
                local_set_1.remove(value)
            elif user_input == 2:
                local_set_2.remove(value)
            else:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again.")


def check_element_action(local_set_1: IntegerSet, local_set_2: IntegerSet) -> None:
    while True:
        try:
            user_input: int = int(input("Enter the set number: "))
            value_my: int = int(input("Enter the element value: "))
            if user_input == 1:
                print(local_set_1.contains(value_my))
            elif user_input == 2:
                print(local_set_2.contains(value_my))
            else:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please try again.")


def get_user_input() -> IntegerSet:
    while True:
        try:
            user_input: str = input("Enter the elements of the set: ")
            user_list = list(map(int, user_input.split()))
            return IntegerSet(user_list)
        except ValueError:
            print("Invalid input. Please try again.")


def menu():
    set_1 = get_user_input()
    set_2 = get_user_input()
    actions = {
        Choice.SHOW_ELEMENTS.value: lambda: show_elements_action(set_1, set_2),
        Choice.SHOW_INTERSECTIONS.value: lambda: show_intersections_action(set_1, set_2),
        Choice.ADD_ELEMENT.value: lambda: add_element_action(set_1, set_2),
        Choice.REMOVE_ELEMENT.value: lambda: remove_element_action(set_1, set_2),
        Choice.CHECK_ELEMENT.value: lambda: check_element_action(set_1, set_2),
    }
    while True:
        print("Menu:")
        for choice in Choice:
            print(f"{choice.value}. {choiceValues[choice.value]}", end="   ")
        print("")
        user_choice: int = int(input("Enter your choice: "))
        if user_choice == Choice.EXIT.value:
            break
        actions[user_choice]()


if __name__ == "__main__":
    menu()

def is_valid(brackets: str) -> bool:
    """
    Проверяет, является ли последовательность скобок корректной.

    Args:
        brackets (str): Строка, содержащая только скобки

    Returns:
        bool: True если последовательность корректна, False в противном случае
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in brackets:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


def main():
    input_string = input("Введите строку, содержащую только скобки: ")
    result = is_valid(input_string)
    print("Результат:", result)


if __name__ == "__main__":
    main()

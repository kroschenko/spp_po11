def is_palindrome(input_str: str) -> bool:
    if not isinstance(input_str, str):
        raise TypeError("Входные данные должны быть строкой")
    try:
        cleaned = ''.join(char.lower() for char in input_str if char.isalnum())
        return cleaned == cleaned[::-1]
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Ошибка при обработке строки: {str(e)}") from e

if __name__ == "__main__":
    try:
        user_input = input("Введите строку для проверки на палиндром: ")
        if is_palindrome(user_input):
            print("Это палиндром!")
        else:
            print("Это не палиндром.")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
    except (KeyboardInterrupt, EOFError) as e:
        print(f"Программа прервана: {e}")

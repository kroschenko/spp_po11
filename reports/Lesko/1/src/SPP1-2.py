def is_palindrome(input_str: str) -> bool:
    cleaned = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    user_input = input("Введите строку для проверки на палиндром: ")

    if is_palindrome(user_input):
        print("Это палиндром!")
    else:
        print("Это не палиндром.")

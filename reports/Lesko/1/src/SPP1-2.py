def is_palindrome(s: str) -> bool:
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    s = input("Введите строку для проверки на палиндром: ")

    if is_palindrome(s):
        print("Это палиндром!")
    else:
        print("Это не палиндром.")
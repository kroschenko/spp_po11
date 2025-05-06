def parse_input(user_input):
    if not user_input.strip():  # Проверяем, что строка не пустая
        raise ValueError("Входная строка не может быть пустой")
    try:
        return list(map(int, user_input.split()))
    except ValueError:
        raise ValueError("Все элементы должны быть целыми числами")

def calculate_range(numbers):
    if not numbers:
        raise ValueError("Список не может быть пустым")
    return max(numbers) - min(numbers)

def main():
    try:
        user_input = input("Введите массив целых чисел через пробел: ")
        numbers_list = parse_input(user_input)
        print("Введенный массив: ", numbers_list, "\n")
        print("Размах последовательности: ", calculate_range(numbers_list), "\n")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

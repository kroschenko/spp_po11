try:
    user_input = input("Введите массив целых чисел через пробел: ")
    numbers_list = list(map(int, user_input.split()))
    print("Введенный массив: ", numbers_list, "\n")
    print("Размах последовательности: ", max(numbers_list) - min(numbers_list), "\n")

except ValueError:
    print("Ошибка: Введите только целые числа.")

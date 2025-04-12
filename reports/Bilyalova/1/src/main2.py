def find_first_occurrence(haystack_str, needle_str):
    return haystack_str.find(needle_str)

input_haystack = input("Введите строку haystack: ")
input_needle = input("Введите строку needle: ")
index = find_first_occurrence(input_haystack, input_needle)

if index != -1:
    print(f"Индекс первого вхождения: {index}")
else:
    print("Подстрока не найдена")
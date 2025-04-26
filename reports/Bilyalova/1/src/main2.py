def find_first_occurrence(main_string, search_string):
    return main_string.find(search_string)


haystack = input("Введите строку haystack: ")
needle = input("Введите строку needle: ")

index = find_first_occurrence(haystack, needle)

if index != -1:
    print(f"Индекс первого вхождения: {index}")
else:
    print("Подстрока не найдена")

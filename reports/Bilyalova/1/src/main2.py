def find_first_occurrence(haystack, needle):
    return haystack.find(needle)


haystack = input("Введите строку haystack: ")
needle = input("Введите строку needle: ")

index = find_first_occurrence(haystack, needle)

if index != -1:
    print(f"Индекс первого вхождения: {index}")
else:
    print(f"Индекс первого вхождения: {index}")

numbers = input("Введите числа через пробел: ")

numbers_list = list(map(int, numbers.split()))

sum_of_squares = sum(x**2 for x in numbers_list if x < 0)

print("Сумма квадратов всех отрицательных чисел:", sum_of_squares)

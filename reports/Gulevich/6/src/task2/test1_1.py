import pytest
from task_1 import find_median


# Тесты для функции find_median
@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3], 2),  # Нечетное количество чисел
        ([1, 2, 3, 4], 2.5),  # Четное количество чисел
        ([5], 5),  # Один элемент
        ([1, 1, 1, 1, 1], 1),  # Все элементы одинаковые
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3.5),  # Большой неотсортированный список
    ],
)
def test_find_median(numbers, expected):
    assert find_median(numbers.copy()) == expected  # Используем копию, так как функция модифицирует список


def test_find_median_empty_list():
    with pytest.raises(IndexError):
        find_median([])


# Тест на типы данных
def test_find_median_invalid_types():
    with pytest.raises(TypeError):
        find_median(["a", "b", "c"])  # Строки вместо чисел


# Тест на граничные значения
def test_find_median_large_numbers():
    assert find_median([1000000000, -1000000000]) == 0


# Тест на отрицательные числа
def test_find_median_negative_numbers():
    assert find_median([-5, -3, -1, -2, -4]) == -3


# Тест на смешанные типы чисел (int и float)
def test_find_median_mixed_types():
    assert find_median([1, 2.5, 3, 4.5]) == 2.75

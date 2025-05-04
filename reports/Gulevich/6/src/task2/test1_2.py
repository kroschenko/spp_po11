import pytest
from task_1_2 import plus_one


# Тесты для функции plus_one
@pytest.mark.parametrize(
    "digits,expected",
    [
        ([1, 2, 3], [1, 2, 4]),  # Обычный случай
        ([9], [1, 0]),  # Однозначное число 9
        ([9, 9, 9], [1, 0, 0, 0]),  # Все цифры 9
        ([1, 9, 9], [2, 0, 0]),  # Некоторые цифры 9
        ([0], [1]),  # Ноль
        ([1, 0, 0], [1, 0, 1]),  # Число с нулями на конце
    ],
)
def test_plus_one(digits, expected):
    result = plus_one(digits.copy())  # Используем копию, так как функция модифицирует список
    assert result == expected


def test_plus_one_empty_list():
    with pytest.raises(IndexError):
        plus_one([])


# Тест на типы данных
def test_plus_one_invalid_types():
    with pytest.raises(TypeError):
        plus_one(["1", "2", "3"])  # Строки вместо чисел


# Тест на граничные значения
def test_plus_one_large_number():
    result = plus_one([9] * 1000)  # Очень большое число из девяток
    assert len(result) == 1001
    assert result[0] == 1
    assert all(x == 0 for x in result[1:])


# Тест на отрицательные числа
def test_plus_one_negative_digits():
    with pytest.raises(ValueError):
        plus_one([-1, 2, 3])  # Отрицательные цифры недопустимы


# Тест на числа больше 9
def test_plus_one_large_digits():
    with pytest.raises(ValueError):
        plus_one([10, 2, 3])  # Цифры больше 9 недопустимы

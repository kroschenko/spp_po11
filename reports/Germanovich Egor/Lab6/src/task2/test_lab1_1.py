import os
import sys
import pytest
from Lab1_1 import calculate_negative_squares_sum
from Lab1_2 import is_valid

# Добавляем путь к директории с исходными файлами в sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
lab1_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))), "Lab1", "src")
sys.path.append(lab1_dir)

# Тесты для функции calculate_negative_squares_sum
@pytest.mark.parametrize("numbers,expected", [
    ([], 0),  # Пустой список
    ([1, 2, 3], 0),  # Только положительные числа
    ([-1, -2, -3], 14),  # Только отрицательные числа
    ([-1, 0, 1], 1),  # Смешанные числа с нулем
    ([-5, 2, -3, 1], 34),  # Смешанные числа
])
def test_calculate_negative_squares_sum(numbers, expected):
    """Тест на корректное вычисление суммы квадратов отрицательных чисел"""
    assert calculate_negative_squares_sum(numbers) == expected

def test_calculate_negative_squares_sum_with_large_numbers():
    """Тест на работу с большими числами"""
    numbers = [-1000, 1000]
    assert calculate_negative_squares_sum(numbers) == 1_000_000

def test_calculate_negative_squares_sum_with_zero():
    """Тест на работу с нулями"""
    numbers = [0, 0, 0]
    assert calculate_negative_squares_sum(numbers) == 0

def test_calculate_negative_squares_sum_with_single_negative():
    """Тест на один отрицательный элемент"""
    numbers = [-5]
    assert calculate_negative_squares_sum(numbers) == 25

def test_calculate_negative_squares_sum_with_single_positive():
    """Тест на один положительный элемент"""
    numbers = [5]
    assert calculate_negative_squares_sum(numbers) == 0

def test_calculate_negative_squares_sum_with_float_numbers():
    """Тест на работу с дробными числами"""
    numbers = [-1.5, 2.5, -3.5]
    assert calculate_negative_squares_sum(numbers) == 14.75

@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("", True),  # Пустая строка
        ("()", True),  # Простые круглые скобки
        ("[]", True),  # Простые квадратные скобки
        ("{}", True),  # Простые фигурные скобки
        ("({[]})", True),  # Вложенные скобки
        ("([)]", False),  # Неправильно вложенные скобки
        ("((", False),  # Незакрытые скобки
        ("))", False),  # Незакрытые скобки с начала
        ("([]{})", True),  # Последовательные правильные скобки
        ("{[()]}", True),  # Сложные вложенные скобки
    ],
)
def test_is_valid_brackets(brackets, expected):
    assert is_valid(brackets) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "a",  # Буква
        "1",  # Цифра
        "( )",  # Пробел
        "([a])",  # Буква внутри скобок
    ],
)
def test_is_valid_with_invalid_chars(invalid_input):
    """Тест на наличие недопустимых символов"""
    assert not is_valid(invalid_input)


def test_is_valid_with_long_sequence():
    """Тест на длинную последовательность скобок"""
    brackets = "(" * 1000 + ")" * 1000
    assert is_valid(brackets)


def test_is_valid_with_mixed_long_sequence():
    """Тест на длинную смешанную последовательность скобок"""
    brackets = "([{" * 100 + "}])" * 100
    assert is_valid(brackets)

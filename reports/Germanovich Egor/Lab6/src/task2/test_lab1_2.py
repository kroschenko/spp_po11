import os
import sys

import pytest

# Добавляем путь к директории с исходными файлами в sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
lab1_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))), "Lab1", "src")
sys.path.append(lab1_dir)

from Lab1_2 import is_valid


# Тесты для проверки корректных последовательностей скобок
@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("", True),  # Пустая строка
        ("()", True),  # Простые круглые скобки
        ("[]", True),  # Простые квадратные скобки
        ("{}", True),  # Простые фигурные скобки
        ("({[]})", True),  # Вложенные скобки
        ("([]{})", True),  # Последовательные правильные скобки
        ("{[()]}", True),  # Сложные вложенные скобки
        ("()[]{}", True),  # Несколько пар скобок
        ("((()))", True),  # Много вложенных круглых скобок
        ("[{()}]", True),  # Смешанные вложенные скобки
    ],
)
def test_valid_brackets_sequences(brackets, expected):
    """Тест на корректные последовательности скобок"""
    assert is_valid(brackets) == expected


# Тесты для проверки некорректных последовательностей скобок
@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("([)]", False),  # Неправильно вложенные скобки
        ("((", False),  # Незакрытые скобки
        ("))", False),  # Незакрытые скобки с начала
        ("({[)", False),  # Неправильное закрытие
        ("]()", False),  # Закрывающая скобка в начале
        ("({)}", False),  # Неправильное вложение
        ("([{}", False),  # Незакрытые скобки
        ("({[}])", False),  # Неправильное закрытие
    ],
)
def test_invalid_brackets_sequences(brackets, expected):
    """Тест на некорректные последовательности скобок"""
    assert is_valid(brackets) == expected


# Тесты на граничные случаи
def test_empty_string():
    """Тест на пустую строку"""
    assert is_valid("") == True


def test_single_opening_bracket():
    """Тест на одну открывающую скобку"""
    assert is_valid("(") == False


def test_single_closing_bracket():
    """Тест на одну закрывающую скобку"""
    assert is_valid(")") == False


# Тесты на длинные последовательности
def test_long_sequence():
    """Тест на длинную последовательность скобок"""
    brackets = "(" * 1000 + ")" * 1000
    assert is_valid(brackets) == True


def test_mixed_long_sequence():
    """Тест на длинную смешанную последовательность скобок"""
    brackets = "([{" * 100 + "}])" * 100
    assert is_valid(brackets) == True


# Тесты на недопустимые символы
@pytest.mark.parametrize(
    "invalid_input",
    [
        "a",  # Буква
        "1",  # Цифра
        "( )",  # Пробел
        "([a])",  # Буква внутри скобок
        "()[]{}a",  # Буква в конце
        "a()[]{}",  # Буква в начале
        "()a[]{}",  # Буква в середине
    ],
)
def test_invalid_characters(invalid_input):
    """Тест на наличие недопустимых символов"""
    assert is_valid(invalid_input) == False


# Тест на производительность
def test_performance():
    """Тест на производительность с очень длинной последовательностью"""
    brackets = "([{" * 10000 + "}])" * 10000
    assert is_valid(brackets) == True

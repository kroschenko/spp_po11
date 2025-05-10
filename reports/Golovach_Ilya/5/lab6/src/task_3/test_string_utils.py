import pytest
from string_utils import indexOfDifference

def test_indexOfDifference_both_none():
    """Проверка на TypeError при обоих аргументах None"""
    with pytest.raises(TypeError, match="Оба аргумента не могут быть None"):
        indexOfDifference(None, None)

def test_indexOfDifference_empty_strings():
    """Сравнение двух пустых строк"""
    assert indexOfDifference("", "") == -1

def test_indexOfDifference_one_empty_string():
    """Сравнение пустой строки с непустой"""
    assert indexOfDifference("", "abc") == 0
    assert indexOfDifference("abc", "") == 0

def test_indexOfDifference_equal_strings():
    """Сравнение одинаковых строк"""
    assert indexOfDifference("abc", "abc") == -1

def test_indexOfDifference_different_strings():
    """Сравнение строк с разницей в середине"""
    assert indexOfDifference("i am a machine", "i am a robot") == 7
    assert indexOfDifference("ab", " abxyz ") == 2
    assert indexOfDifference(" abcde ", " abxyz ") == 2
    assert indexOfDifference(" abcde ", "xyz") == 0

def test_indexOfDifference_whitespace_handling():
    """Сравнение строк с пробелами"""
    assert indexOfDifference("abc ", " abc ") == -1

def test_indexOfDifference_different_lengths():
    """Сравнение строк разной длины"""
    assert indexOfDifference("short", "shorter") == 5
    assert indexOfDifference("longer", "long") == 4

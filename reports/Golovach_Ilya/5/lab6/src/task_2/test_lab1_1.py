import pytest
from lab1_1 import parse_input, calculate_range

def test_parse_input_valid():
    assert parse_input("1 2 3") == [1, 2, 3]
    assert parse_input("-5 0 5") == [-5, 0, 5]
    assert parse_input("100") == [100]

def test_parse_input_invalid():
    with pytest.raises(ValueError, match="Все элементы должны быть целыми числами"):
        parse_input("1 2 abc")
    with pytest.raises(ValueError, match="Все элементы должны быть целыми числами"):
        parse_input("1.5 2 3")
    with pytest.raises(ValueError, match="Входная строка не может быть пустой"):
        parse_input("")  # Теперь это вызывает исключение

def test_calculate_range():
    assert calculate_range([1, 2, 3]) == 2
    assert calculate_range([-5, 0, 5]) == 10
    assert calculate_range([100]) == 0
    assert calculate_range([5, 5, 5]) == 0

def test_calculate_range_empty():
    with pytest.raises(ValueError, match="Список не может быть пустым"):
        calculate_range([])

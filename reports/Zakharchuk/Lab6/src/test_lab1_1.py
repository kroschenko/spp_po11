import pytest

from lab1_1 import parse_numbers, calculate_average, count_above_average, calculate_percentage


def test_parse_numbers_valid():
    assert parse_numbers("1 2 3") == [1, 2, 3]
    assert parse_numbers("0") == [0]
    assert parse_numbers("-1 0 1") == [-1, 0, 1]


def test_parse_numbers_invalid():
    with pytest.raises(ValueError, match="Все элементы должны быть целыми числами"):
        parse_numbers("1 2 a")
    with pytest.raises(ValueError, match="Все элементы должны быть целыми числами"):
        parse_numbers("1.5 2 3")


def test_parse_numbers_empty():
    with pytest.raises(ValueError, match="Все элементы должны быть целыми числами"):
        parse_numbers("")


def test_calculate_average_normal():
    assert calculate_average([1, 2, 3]) == 2.0
    assert calculate_average([10]) == 10.0
    assert calculate_average([-1, 0, 1]) == 0.0


def test_calculate_average_empty():
    with pytest.raises(ValueError, match="Список чисел не может быть пустым"):
        calculate_average([])


def test_count_above_average_normal():
    numbers = [1, 2, 3, 4]
    average = 2.5
    assert count_above_average(numbers, average) == 2  # 3 и 4 больше 2.5
    assert count_above_average([1], 1.0) == 0  # Нет чисел больше 1.0
    assert count_above_average([1, 1, 1], 1.0) == 0  # Нет чисел больше 1.0


def test_count_above_average_all_above():
    assert count_above_average([2, 3, 4], 1.0) == 3


def test_count_above_average_none_above():
    assert count_above_average([1, 2, 3], 5.0) == 0


def test_calculate_percentage_normal():
    assert calculate_percentage(2, 4) == 50.0
    assert calculate_percentage(0, 5) == 0.0
    assert calculate_percentage(1, 1) == 100.0


def test_calculate_percentage_zero_total():
    with pytest.raises(ValueError, match="Общее количество не может быть нулевым"):
        calculate_percentage(1, 0)

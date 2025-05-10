import pytest
from SPP1_1 import rep

def test_normal_case():
    """Тест нормального случая с положительными числами"""
    assert rep(1, 5, 1) == [1, 2, 3, 4]

def test_negative_numbers():
    """Тест с отрицательными числами"""
    assert rep(-5, -1, 1) == [-5, -4, -3, -2]

def test_empty_sequence():
    """Тест случая, когда последовательность пуста"""
    assert rep(1, 2, 2) == [1]

def test_single_element():
    """Тест случая с одним элементом"""
    assert rep(1, 3, 2) == [1]

def test_zero_step():
    """Тест случая с нулевым шагом"""
    with pytest.raises(ValueError, match="шаг не может быть равен нулю"):
        rep(1, 5, 0)

def test_negative_step():
    """Тест случая с отрицательным шагом"""
    with pytest.raises(ValueError, match="шаг должен быть положительным"):
        rep(1, 5, -1)

def test_start_greater_than_end():
    """Тест случая, когда начало больше конца"""
    with pytest.raises(ValueError, match="start должен быть меньше end"):
        rep(5, 1, 1)

def test_start_equals_end():
    """Тест случая, когда начало равно концу"""
    with pytest.raises(ValueError, match="start должен быть меньше end"):
        rep(5, 5, 1)

def test_large_numbers():
    """Тест с большими числами"""
    assert rep(1000000, 1000005, 1) == [1000000, 1000001, 1000002, 1000003, 1000004]

@pytest.mark.parametrize("start,end,step,expected", [
    (1, 5, 1, [1, 2, 3, 4]),
    (-5, -1, 1, [-5, -4, -3, -2]),
    (1, 2, 2, [1]),
    (1, 3, 2, [1]),
])
def test_rep_parametrized(start, end, step, expected):
    """Параметризованный тест для различных случаев"""
    assert rep(start, end, step) == expected

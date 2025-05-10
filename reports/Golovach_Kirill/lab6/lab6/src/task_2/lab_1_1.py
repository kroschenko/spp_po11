import pytest
from lab_1_1 import get_positive_integer, get_numbers_from_user, shuffle_numbers
from unittest.mock import patch


@pytest.fixture
def mock_input():
    """Fixture to mock the input() function."""
    with patch('builtins.input') as mock:
        yield mock


def test_get_positive_integer_valid_input(mock_input):
    """Test that get_positive_integer returns correct value for valid input."""
    mock_input.return_value = "5"
    result = get_positive_integer("Enter a number: ")
    assert result == 5
    mock_input.assert_called_once_with("Enter a number: ")


def test_get_positive_integer_negative_input(mock_input):
    """Test that get_positive_integer rejects negative numbers."""
    mock_input.side_effect = ["-5", "0", "5"]  # Негативный тест с исправлением
    result = get_positive_integer("Enter a number: ")
    assert result == 5
    assert mock_input.call_count == 3


def test_get_positive_integer_non_numeric_input(mock_input):
    """Test that get_positive_integer rejects non-numeric input."""
    mock_input.side_effect = ["abc", "5"]  # Нечисловой ввод с исправлением
    result = get_positive_integer("Enter a number: ")
    assert result == 5
    assert mock_input.call_count == 2


def test_get_numbers_from_user(mock_input):
    """Test that get_numbers_from_user collects correct numbers."""
    mock_input.side_effect = ["10", "20", "30"]
    numbers = get_numbers_from_user(3)
    assert numbers == [10, 20, 30]
    assert mock_input.call_count == 3


def test_shuffle_numbers():
    """Test that shuffle_numbers actually shuffles the list."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_numbers(original.copy())
    assert set(original) == set(shuffled)  # Проверяем те же элементы
    assert original != shuffled  # Но порядок должен измениться


def test_main_full_flow(mock_input):
    """Integration test for the main workflow."""
    mock_input.side_effect = ["3", "10", "20", "30"]  # N=3 и три числа
    with patch('lab_1_1.print') as mock_print:
        with patch('lab_1_1.main') as mock_main:
            import lab_1_1
            lab_1_1.main()

    # Проверяем что все вызовы input были сделаны
    assert mock_input.call_count == 4
    # Проверяем что print был вызван с перемешанными числами
    assert mock_print.called

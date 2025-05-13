import unittest
from unittest.mock import patch
from lab_1_1 import get_positive_integer, get_numbers_from_user, shuffle_numbers, main


class TestLab1Functions(unittest.TestCase):

    @patch('builtins.input', return_value="5")
    def test_get_positive_integer_valid(self, mock_input):
        """Тест корректного ввода положительного числа."""
        result = get_positive_integer("Введите число: ")
        self.assertEqual(result, 5)
        mock_input.assert_called_once_with("Введите число: ")

    @patch('builtins.input', side_effect=["-3", "0", "5"])
    def test_get_positive_integer_invalid(self, mock_input):
        """Тест обработки некорректного ввода."""
        result = get_positive_integer("Введите число: ")
        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=["abc", "5"])
    def test_get_positive_integer_non_numeric(self, mock_input):
        """Тест обработки нечислового ввода."""
        result = get_positive_integer("Введите число: ")
        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.input', side_effect=["1", "2", "3"])
    def test_get_numbers_from_user(self, mock_input):
        """Тест ввода списка чисел."""
        result = get_numbers_from_user(3)
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(mock_input.call_count, 3)

    def test_shuffle_numbers(self):
        """Тест перемешивания чисел."""
        original = [1, 2, 3, 4, 5]
        shuffled = shuffle_numbers(original.copy())
        self.assertNotEqual(original, shuffled)
        self.assertCountEqual(original, shuffled)

    @patch('builtins.input', side_effect=["2", "10", "20"])
    @patch('lab_1_1.print')
    def test_main_workflow(self, mock_print, mock_input):
        """Интеграционный тест основного workflow."""
        main()
        self.assertEqual(mock_input.call_count, 3)
        self.assertTrue(mock_print.called)


if __name__ == "__main__":
    unittest.main()

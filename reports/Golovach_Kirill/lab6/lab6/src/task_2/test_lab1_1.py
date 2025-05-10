import unittest
from unittest.mock import patch  # Явно импортируем mock
from lab_1_1 import get_positive_integer, get_numbers_from_user, shuffle_numbers

class TestLab1Functions(unittest.TestCase):

    @patch('builtins.input', return_value="5")
    def test_get_positive_integer_valid(self, mock_input):
        """
        Тест на корректный ввод положительного числа.
        Проверяет, что функция возвращает ожидаемое значение при корректном вводе.
        """
        self.assertEqual(get_positive_integer("Введите число: "), 5)

    @patch('builtins.input', side_effect=["-3", "0", "5"])
    def test_get_positive_integer_invalid(self, mock_input):
        """
        Тест на некорректный ввод (отрицательное число или ноль).
        Проверяет, что функция продолжает запрашивать ввод до тех пор,
        пока не будет введено положительное число.
        """
        self.assertEqual(get_positive_integer("Введите число: "), 5)

    @patch('builtins.input', side_effect=["1", "2", "3"])
    def test_get_numbers_from_user(self, mock_input):
        """
        Тест на корректный ввод списка чисел.
        Проверяет, что функция корректно обрабатывает последовательность ввода.
        """
        self.assertEqual(get_numbers_from_user(3), [1, 2, 3])

    def test_shuffle_numbers(self):
        """
        Тест на перемешивание чисел.
        Проверяет, что список после перемешивания содержит те же элементы,
        но в другом порядке.
        """
        numbers = [1, 2, 3, 4, 5]
        shuffled = shuffle_numbers(numbers.copy())
        self.assertNotEqual(numbers, shuffled)  # Проверяем, что порядок изменился
        self.assertCountEqual(numbers, shuffled)  # Проверяем, что элементы те же

if __name__ == "__main__":
    unittest.main()

import unittest
from lab_2_2 import majority_element

class TestMajorityElement(unittest.TestCase):

    def test_majority_element_basic(self):
        """Тест на базовые случаи."""
        self.assertEqual(majority_element([3, 2, 3]), 3)
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_majority_element_single_element(self):
        """Тест на массив с одним элементом."""
        self.assertEqual(majority_element([5]), 5)

    def test_majority_element_all_same(self):
        """Тест на массив, где все элементы одинаковые."""
        self.assertEqual(majority_element([7, 7, 7, 7, 7]), 7)

    def test_majority_element_edge_cases(self):
        """Тест на граничные случаи."""
        self.assertEqual(majority_element([1, 2, 1]), 1)
        self.assertEqual(majority_element([1, 1, 2, 2, 1]), 1)

    def test_majority_element_large_input(self):
        """Тест на большой массив."""
        nums = [1] * 5000 + [2] * 4999
        self.assertEqual(majority_element(nums), 1)

if __name__ == "__main__":
    unittest.main()

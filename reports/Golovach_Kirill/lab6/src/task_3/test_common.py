import unittest

from src.task_3.common import common


class TestCommonMethod(unittest.TestCase):

    def test_common_with_none(self):
        """Тест на передачу None в качестве аргументов."""
        with self.assertRaises(TypeError):
            common(None, None)

    def test_common_empty_strings(self):
        """Тест на пустые строки."""
        self.assertEqual(common("", ""), "")

    def test_common_one_empty_string(self):
        """Тест на одну пустую строку."""
        self.assertEqual(common("", "abc"), "")
        self.assertEqual(common("abc", ""), "")

    def test_common_identical_strings(self):
        """Тест на идентичные строки."""
        self.assertEqual(common("abc", "abc"), "abc")

    def test_common_partial_overlap(self):
        """Тест на частичное совпадение."""
        self.assertEqual(common("ab", "abxyz"), "ab")
        self.assertEqual(common("abcde", "abxyz"), "ab")

    def test_common_no_overlap(self):
        """Тест на отсутствие совпадений."""
        self.assertEqual(common("abcde", "xyz"), "")

    def test_common_substring_in_middle(self):
        """Тест на подстроку в середине."""
        self.assertEqual(common("deabc", "abcdeabcd"), "deabc")

    def test_common_complex_overlap(self):
        """Тест на сложное пересечение."""
        self.assertEqual(common("dfabcegt", "rtoefabceiq"), "fabce")

if __name__ == "__main__":
    unittest.main()

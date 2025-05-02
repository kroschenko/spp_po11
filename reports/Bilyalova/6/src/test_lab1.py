import pytest
import sys
import os
from pathlib import Path

lab1_path = str(Path(__file__).parent.parent.parent / "1" / "src")
sys.path.insert(0, lab1_path)

from main import find_modes
from main2 import find_first_occurrence

class TestFindModes:
    def test_empty_sequence(self):
        assert find_modes([]) is None
    
    def test_no_mode(self):
        assert find_modes([1, 2, 3]) is None
    
    def test_single_mode(self):
        assert find_modes([1, 2, 2, 3]) == [2]
    
    def test_multiple_modes(self):
        result = find_modes([1, 1, 2, 2, 3])
        assert sorted(result) == [1, 2]
    
    def test_all_elements_same(self):
        assert find_modes([5, 5, 5]) == [5]
    
    def test_negative_numbers(self):
        assert find_modes([-1, -1, -2]) == [-1]
    
    def test_single_element(self):
        assert find_modes([7]) is None
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            find_modes([1, 2, {}])

class TestFindFirstOccurrence:
    def test_normal_case(self):
        assert find_first_occurrence("hello world", "world") == 6
    
    def test_not_found(self):
        assert find_first_occurrence("hello", "world") == -1
    
    def test_empty_needle(self):
        assert find_first_occurrence("hello", "") == 0
    
    def test_empty_haystack(self):
        assert find_first_occurrence("", "hello") == -1
    
    def test_both_empty(self):
        assert find_first_occurrence("", "") == 0
    
    def test_multiple_occurrences(self):
        assert find_first_occurrence("ababab", "ab") == 0
    
    def test_case_sensitive(self):
        assert find_first_occurrence("Hello", "hello") == -1
    
    def test_unicode(self):
        assert find_first_occurrence("привет мир", "мир") == 7
    
    def test_none_input(self):
        assert find_first_occurrence(None, "test") == -1
        assert find_first_occurrence("test", None) == -1
        assert find_first_occurrence(None, None) == -1
    
    def test_non_string_input(self):
        assert find_first_occurrence(123, "23") == -1
        assert find_first_occurrence("hello", 123) == -1

def test_main_input_handling(monkeypatch):
    inputs = iter(["3", "1", "2", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    from main import main
    main()

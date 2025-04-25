import pytest
from task_1 import find_unique_numbers


def test_trivial_cases():
    assert find_unique_numbers([1, 2, 2, 3, 4, 4]) == {1, 2, 3, 4}
    assert find_unique_numbers([1, 2, 3, 4]) == {1, 2, 3, 4}


def test_boundary_cases():
    assert find_unique_numbers([]) == set()
    assert find_unique_numbers([5]) == {5}
    assert find_unique_numbers([5, 5, 5]) == {5}


def test_non_list_input():
    with pytest.raises(TypeError):
        find_unique_numbers("123")


def test_list_with_non_numeric_input():
    with pytest.raises(TypeError):
        find_unique_numbers([1, "a", 3])


def test_list_with_mixed_types():
    with pytest.raises(TypeError):
        find_unique_numbers([1, 2.5, 3])

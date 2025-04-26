import pytest
from Z2 import two_sum


def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_single_element_equals_target():
    assert two_sum([5], 5) == []


def test_no_pair():
    assert two_sum([1, 2, 3], 7) == []
    assert two_sum([], 5) == []
    assert two_sum([1], 2) == []


def test_multiple_pairs():
    result = two_sum([1, 3, 2, 4], 6)
    assert result in ([1, 3], [2, 3])


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert two_sum([-1, 2, 3, 4], 1) == [0, 1]


def test_zero_target():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]


def test_duplicates():
    assert two_sum([1, 5, 5, 3], 10) == [1, 2]


def test_non_integer_numbers():
    assert two_sum([1.5, 3.5, 2.0], 5.0) == [0, 1]


def test_invalid_input():
    with pytest.raises(TypeError):
        two_sum(None, 5)
    with pytest.raises(TypeError):
        two_sum(123, 5)

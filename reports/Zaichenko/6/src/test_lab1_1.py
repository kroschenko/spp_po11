import os
import sys
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
lab1_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "1", "src"))
sys.path.append(lab1_dir)

from lab1_1 import find_the_max


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 2, 3], {1: 1, 2: 1}),
        ([2, 2, 3], {1: 0, 2: 1}),
        ([-2, 0, 2], {0: 2, 2: 2}),
        ([0, 0, 0], {1: 0, 2: 0}),
        ([5, 3, 4], {1: 1, 2: 1}),
        ([1, 1, 1, 1], {1: 0, 2: 0, 3: 0}),
        ([10 ** 6, 10 ** 6 + 1], {1: 1}),
        ([-5, 1], {0: 4}),
        ([1, -5], {0: 4}),
        ([-1, -5], {0: 4}),
        ([-3, -1, 5], {0: 2, 2: 4})
    ]
)
def test_valid_numeric_sequences(numbers, expected):
    assert find_the_max(numbers) == expected


@pytest.mark.parametrize(
    "invalid_input_for_type_error",
    [
        [1, "a"],
        ["a", 1],
        ["a", "b"],
        ["(", ")"],
        [1, 2, "a"],
        ["1", "2", {}],
        [1, None],
        [None, 1],
        [None, None],
    ]
)
def test_inputs_causing_type_error(invalid_input_for_type_error):
    with pytest.raises(TypeError):
        find_the_max(invalid_input_for_type_error)


@pytest.mark.parametrize(
    "single_element_input",
    [
        ["a"],
        ["()"],
        [None],
        [{}],
        [[1, 2]],
    ]
)
def test_single_element_various_types_returns_empty_dict(single_element_input):
    assert find_the_max(single_element_input) == {}


def test_empty_list_boundary():
    assert find_the_max([]) == {}


def test_single_numeric_element_list_boundary():
    assert find_the_max([1]) == {}
    assert find_the_max([-100]) == {}
    assert find_the_max([0]) == {}


@pytest.mark.parametrize(
    "two_elements_input, expected_two_elements",
    [
        ([5, 10], {1: 5}),
        ([10, 5], {1: 5}),
        ([-10, 5], {0: 5}),
        ([5, -10], {0: 5}),
        ([-5, -10], {0: 5}),
        ([-10, -5], {0: 5}),
        ([0, 0], {1: 0}),
        ([5, 5], {1: 0}),
        ([-5, -5], {1: 0}),
    ]
)
def test_two_elements_list_boundary(two_elements_input, expected_two_elements):
    assert find_the_max(two_elements_input) == expected_two_elements

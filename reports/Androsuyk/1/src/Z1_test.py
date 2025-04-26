from Z1 import check_sequence


def test_all_equal():
    assert check_sequence([1, 1, 1, 1]) == "равны"
    assert check_sequence([0, 0, 0]) == "равны"
    assert check_sequence(["a", "a", "a"]) == "равны"


def test_not_all_equal():
    assert check_sequence([1, 2, 1, 1]) == "не равны"
    assert check_sequence([0, 1]) == "не равны"
    assert check_sequence(["a", "b", "a"]) == "не равны"


def test_single_element():
    assert check_sequence([42]) == "равны"


def test_empty_sequence():
    assert check_sequence([]) == "пустая последовательность"


def test_non_list_input():
    assert check_sequence((2, 2, 2)) == "равны"
    assert check_sequence("aaa") == "равны"

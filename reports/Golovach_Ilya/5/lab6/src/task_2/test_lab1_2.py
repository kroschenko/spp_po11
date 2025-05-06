from lab1_2 import longest_common_prefix

def test_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["apple", "apple", "apple"]) == "apple"
    assert longest_common_prefix(["", "test", "test"]) == ""
    assert longest_common_prefix(["prefix", "preference", "preform"]) == "pref"

def test_edge_cases():
    assert longest_common_prefix([""]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["", ""]) == ""

def test_empty_input():
    assert longest_common_prefix([]) == ""

def test_different_cases():
    assert longest_common_prefix(["Python", "python"]) == ""
    assert longest_common_prefix(["Test", "TEst", "TEST"]) == "T"

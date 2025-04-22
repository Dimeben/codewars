from simple_calculator import calculator


def test_addition():
    assert calculator(1, 2, "+") == 3


def test_subtraction():
    assert calculator(6, 2, "-") == 4


def test_division():
    assert calculator(10, 5, "/") == 2


def test_multiplication():
    assert calculator(6, 2, "x") == 12


def test_invalid_operation():
    assert calculator(1, 1, "&") == "unknown value"


def test_invalid_numbers():
    assert calculator("!", 1, "+") == "unknown value"
    assert calculator(1, "D", "+") == "unknown value"

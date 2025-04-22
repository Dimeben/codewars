from does_my_number_look_big_in_this import narcissistic


def test_true_narcissistic():
    assert narcissistic(153) == True
    assert narcissistic(371) == True


def test_false_narcissistic():
    assert narcissistic(122) == False
    assert narcissistic(4887) == False

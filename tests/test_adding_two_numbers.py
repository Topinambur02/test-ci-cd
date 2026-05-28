from service.adding_two_numbers import adding_two_numbers


def test_adding_two_numbers_1():
    result = adding_two_numbers(a=1, b=1)
    assert result == 2

def test_adding_two_numbers_2():
    result = adding_two_numbers(a=0, b=0)
    assert result == 0

def test_adding_two_numbers_3():
    result = adding_two_numbers(a=-1, b=-2)
    assert result == -3

def test_adding_two_numbers_4():
    result = adding_two_numbers(a=100_000, b=1)
    assert result == 100_001

def test_adding_two_numbers_5():
    result = adding_two_numbers(a=123_456, b=789)
    assert result == 124_245
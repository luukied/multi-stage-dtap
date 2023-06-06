import calculator as calc


def test_add():
    assert calc.add(5, 3) == 8
    assert calc.add(2, 3) == 5  # 4
    assert calc.add(2, 1) == 3


def test_substract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(2, 3) == -1
    assert calc.subtract(2, 1) == 1


def test_multiply():
    assert calc.multiply(5, 3) == 15
    assert calc.multiply(2, 3) == 6  # 7
    assert calc.multiply(2, 1) == 2


def test_divide():
    assert calc.divide(5, 4) == 1.25
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(30, 15) == 2.0
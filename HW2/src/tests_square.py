import random, pytest
from Square import Square


def GenerateNumberGreaterThanZero():
    return random.randint(1, 10)


def GenerateNumberMinusThanZero():
    return random.randint(-10, 0)


class TestRectangle:
    def test_rectangle_get_area_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        s = Square(value_a)
        assert s.get_area() == value_a ** 2, f"value_a generated = {value_a}"

    def test_rectangle_get_perimeter_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        s = Square(value_a)
        assert s.get_perimeter() == 2 * (value_a + value_a), f"value_a generated = {value_a}"

    def test_rectangle_negative(self):
        value_a = GenerateNumberMinusThanZero()
        with pytest.raises(ValueError):
            Square(value_a)

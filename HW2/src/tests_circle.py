import random, pytest
from Circle import Circle


def GenerateNumberGreaterThanZero():
    return random.randint(1, 10)


def GenerateNumberMinusThanZero():
    return random.randint(-10, 0)


class TestCircle:
    def test_circle_get_area_int_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        c = Circle(value_a)
        assert c.get_area() == value_a * value_a * 3.14, f"value_a generated = {value_a}"

    def test_circle_get_perimeter_int_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        c = Circle(value_a)
        assert c.get_perimeter() == 3.14 * 2 * value_a, f"value_a generated = {value_a}"

    def test_circle_int_negative(self):
        value_a = GenerateNumberMinusThanZero()
        with pytest.raises(ValueError):
            Circle(value_a)

import random, pytest
from Rectangle import Rectangle



def GenerateNumberGreaterThanZero():
    return random.randint(1, 10)


def GenerateNumberMinusThanZero():
    return random.randint(-10, 0)


class TestRectangle:
    def test_rectangle_get_area_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        value_b = GenerateNumberGreaterThanZero()
        r = Rectangle(value_a, value_b)
        assert r.get_area() == value_a * value_b

    def test_rectangle_get_area_negative(self):
        value_a = GenerateNumberMinusThanZero()
        value_b = GenerateNumberGreaterThanZero()
        with pytest.raises(ValueError):
            Rectangle(value_a, value_b)

    def test_rectangle_get_perimeter_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        value_b = GenerateNumberGreaterThanZero()
        r = Rectangle(value_a, value_b)
        assert r.get_perimeter() == 2 * (value_a + value_b)

    def test_rectangle_get_perimeter_negative(self):
        value_a = GenerateNumberMinusThanZero()
        value_b = GenerateNumberGreaterThanZero()
        with pytest.raises(ValueError):
            Rectangle(value_a, value_b)



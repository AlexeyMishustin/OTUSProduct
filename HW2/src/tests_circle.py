import random, pytest
from Circle import Circle


def GenerateNumberGreaterThanZero():
    return random.randint(1, 10)


def GenerateNumberMinusThanZero():
    return random.randint(-10, 0)


class TestCircle:
    def test_circle_get_area_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        c = Circle(value_a)
        assert c.get_area() == value_a * value_a * 3.14

    def test_circle_get_area_negative(self):
        value_a = random.randint(-10, 0)
        with pytest.raises(ValueError):
            Circle(value_a)

    def test_circle_get_perimeter_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        c = Circle(value_a)
        assert c.get_perimeter() == 3.14 * 2 * value_a

    def test_circle_get_perimeter_negative(self):
        value_a = GenerateNumberMinusThanZero()
        with pytest.raises(ValueError):
            Circle(value_a)

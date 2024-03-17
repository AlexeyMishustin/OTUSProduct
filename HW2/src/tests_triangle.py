import random, pytest
from Triangle import Triangle
from math import sqrt



def GenerateNumberGreaterThanZero():
    return random.randint(1, 10)


def GenerateNumberMinusThanZero():
    return random.randint(-10, 0)


class TestTriangle:
    def test_Triangle_get_area_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        value_b = GenerateNumberGreaterThanZero()
        value_c = GenerateNumberGreaterThanZero()
        t = Triangle(value_a, value_b,value_c)
        p = 0.5 * (value_a + value_b + value_c)
        assert t.get_area() == sqrt(p * (p - value_a) * (p - value_b) * (p - value_c))

    def test_Triangle_get_area_negative(self):
        value_a = GenerateNumberMinusThanZero()
        value_b = GenerateNumberGreaterThanZero()
        value_c = GenerateNumberGreaterThanZero()
        with pytest.raises(ValueError):
            Triangle(value_a, value_b,value_c)

    def test_Triangle_get_perimeter_positive(self):
        value_a = GenerateNumberGreaterThanZero()
        value_b = GenerateNumberGreaterThanZero()
        value_c = GenerateNumberGreaterThanZero()
        t = Triangle(value_a, value_b,value_c)
        assert t.get_perimeter() == value_a + value_b + value_c

    def test_Triangle_get_perimeter_negative(self):
        value_a = GenerateNumberMinusThanZero()
        value_b = GenerateNumberGreaterThanZero()
        value_c = GenerateNumberGreaterThanZero()
        with pytest.raises(ValueError):
            Triangle(value_a, value_b, value_c)

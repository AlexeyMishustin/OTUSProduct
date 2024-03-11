from math import sqrt
from Figura import Figure


class Triangle(Figure):
    def __init__(self, value_a: int, value_b: int, value_c: int):
        if value_a <= 0 or value_b <= 0 or value_c <= 0:
            raise ValueError("В один из аргументов передано некорректное значение вх.параметра")
        super().__init__(name="Triangle")
        self.value_a = value_a
        self.value_b = value_b
        self.value_c = value_c

    def get_area(self):
        p = 0.5 * (self.value_a + self.value_b + self.value_c)
        return sqrt(p * (p - self.value_a) * (p - self.value_b) * (p - self.value_c))

    def get_perimeter(self):
        return self.value_a + self.value_b + self.value_c


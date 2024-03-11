from Figura import Figure


class Rectangle(Figure):
    def __init__(self, value_a: int, value_b: int):
        if value_a <= 0 or value_b <= 0:
            raise ValueError("Переданы некорректные вх.параметры")
        super().__init__(name="Rectangle")
        self.value_a = value_a
        self.value_b = value_b

    def get_area(self) -> int:
        return self.value_a * self.value_b

    def get_perimeter(self) -> int:
        return 2 * (self.value_a + self.value_b)

from Figura import Figure


class Circle(Figure):
    def __init__(self, value_a: int):
        if value_a <= 0:
            raise ValueError("Передан некорректный радиус")
        super().__init__(name="Circle")
        self.value_a = value_a

    def get_area(self):
        return 3.14 * self.value_a * self.value_a

    def get_perimeter(self):
        return 3.14 * 2 * self.value_a

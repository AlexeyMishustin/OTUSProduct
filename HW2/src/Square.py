from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, value_a: int):
        if value_a <= 0:
            raise ValueError("Передано некорректное значение вх.параметра")
        super().__init__(value_a=value_a, value_b=value_a)
        self.name = "Square"

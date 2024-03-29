from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def add_area(self, new_figure):
        if not isinstance(new_figure, Figure):
            raise ValueError("Фигура не принадлежит классу Figure")
        return self.get_area() + new_figure.get_area()

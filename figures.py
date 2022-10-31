import abc
from math import sqrt, sin, radians, pi, tan

# /********************************************************************
# * Project Name : zadanie2tp
# * File Name : app.py
# * Programmer : Laypanov Nazim, Volkov Dmitriy, Shuvaev Danila
# * Created : 12 / 10 / 22
# * Last Revision : 22 / 10 / 21
# ********************************************************************/


class Figure(abc.ABC):
    title = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative")
            setattr(self, key, value)

    @classmethod
    def get_title(cls):
        return cls.title


class Figure3D(Figure):
    title = '3D Фигура'

    def get_volume(self):
        return round(self.side ** 3, 4)


class FigureWithArea(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass


class Square(Figure, FigureWithArea):
    title = 'Квадрат'

    def get_area(self):
        return round(self.side ** 2, 4)


class Rectangle(Figure):
    title = 'Прямоугольник'

    def get_area(self):
        return round(self.length * self.width, 4)


class Triangle(Figure, FigureWithArea):
    title = 'Треугольник'

    def get_area(self):
        return round(0.5 * self.side_a * self.side_b * sin(radians(self.angle)), 4)

    @staticmethod
    def check(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False


class Trapezoid(Figure, FigureWithArea):
    title = 'Трапеция'

    def get_area(self):
        return 0.5 * self.height * (self.upper_base + self.lower_base)


class Rhomb(Figure, FigureWithArea):
    title = 'Ромб'

    def get_area(self):
        return round(self.side ** 2 * sin(radians(self.angle)), 4)


class Circle(Figure, FigureWithArea):
    title = 'Круг'

    def get_area(self):
        return round(pi * self.radius ** 2, 4)


class Pyramid(Figure3D, FigureWithArea):
    title = 'Пирамида'

    def get_area(self):
        return round((self.base_side * 4) / 2 * sqrt((self.height ** 2) +
                                                     (self.base_side / (2 * tan(radians(180 / 4)))) ** 2), 4)

    def get_volume(self):
        return round((1 / 3) * self.height * self.base_side ** 2, 4)


class Cube(Figure3D, FigureWithArea):
    title = 'Куб'

    def get_area(self):
        return round(6 * self.side ** 2, 4)


class Sphere(Figure3D, FigureWithArea):
    title = 'Сфера'

    def get_area(self):
        return round(4 * pi * self.radius ** 2, 4)

    def get_volume(self):
        return round((4 / 3) * pi * self.radius ** 3, 4)


class Parallelepiped(Figure3D, FigureWithArea):
    title = 'Параллелепипед'

    def get_area(self):
        return round(2 * (self.length * self.width + self.length * self.height + self.height * self.width), 4)

    def get_volume(self):
        return round(self.length * self.width * self.height, 4)


class Cylinder(Figure3D, FigureWithArea):
    title = 'Цилиндр'

    def get_area(self):
        return round(2 * pi * self.radius * (self.radius + self.height), 4)

    def get_volume(self):
        return round(pi * (self.radius ** 2) * self.height, 4)


class Cone(Figure3D, FigureWithArea):
    title = 'Конус'

    def get_area(self):
        return round(pi * self.radius * sqrt(self.radius ** 2 + self.height ** 2), 4)

    def get_volume(self):
        return round((1 / 3) * (pi * (self.radius ** 2) * self.height), 4)

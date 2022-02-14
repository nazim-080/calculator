from math import sqrt, sin, radians, pi, tan


class Figure:
    _title = 'Фигура'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative")
            setattr(self, key, value)

    @classmethod
    def get_title(cls):
        return cls._title

    @staticmethod
    def print_l():
        print('l')

    def get_area(self):
        pass


class Figure3D(Figure):
    _title = '3D Фигура'

    def get_volume(self):
        pass


class Square(Figure):
    _title = 'Квадрат'

    def get_area(self):
        return round(self.side ** 2, 4)


class Rectangle(Figure):
    _title = 'Прямоугольник'

    def get_area(self):
        return round(self.length * self.width, 4)


class Triangle(Figure):
    _title = 'Треугольник'

    def get_area(self):
        return round(0.5 * self.side_a * self.side_b * sin(radians(self.angle)), 4)

    @staticmethod
    def check(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False


class Trapezoid(Figure):
    _title = 'Трапеция'

    def get_area(self):
        return 0.5 * self.height * (self.upper_base + self.lower_base)


class Rhomb(Figure):
    _title = 'Ромб'

    def get_area(self):
        return round(self.side ** 2 * sin(radians(self.angle)), 4)


class Circle(Figure):
    _title = 'Круг'

    def get_area(self):
        return round(pi * self.radius ** 2, 4)


class Pyramid(Figure3D):
    _title = 'Пирамида'

    def get_area(self):
        return round((self.base_side * 4) / 2 * sqrt((self.height ** 2) +
                                                     (self.base_side / (2 * tan(radians(180 / 4)))) ** 2), 4)

    def get_volume(self):
        return round((1 / 3) * self.height * self.base_side ** 2, 4)


class Cube(Figure3D):
    _title = 'Куб'

    def get_area(self):
        return round(6 * self.side ** 2, 4)

    def get_volume(self):
        return round(self.side ** 3, 4)


class Sphere(Figure3D):
    _title = 'Сфера'

    def get_area(self):
        return round(4 * pi * self.radius ** 2, 4)

    def get_volume(self):
        return round((4 / 3) * pi * self.radius ** 3, 4)


class Parallelepiped(Figure3D):
    _title = 'Параллелепипед'

    def get_area(self):
        return round(2 * (self.length * self.width + self.length * self.height + self.height * self.width), 4)

    def get_volume(self):
        return round(self.length * self.width * self.height, 4)


class Cylinder(Figure3D):
    _title = 'Цилиндр'

    def get_area(self):
        return round(2 * pi * self.radius * (self.radius + self.height), 4)

    def get_volume(self):
        return round(pi * (self.radius ** 2) * self.height, 4)


class Cone(Figure3D):
    _title = 'Конус'

    def get_area(self):
        return round(pi * self.radius * sqrt(self.radius ** 2 + self.height ** 2), 4)

    def get_volume(self):
        round((1 / 3) * (pi * (self.radius ** 2) * self.height), 4)

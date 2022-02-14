from math import sqrt, sin, radians, pi, tan


class Figure:
    _title = 'Фигура'

    @classmethod
    def get_title(cls):
        return cls._title

    def area(self):
        pass


class Figure3D(Figure):
    _title = '3D Фигура'

    def volume(self):
        pass


class Square(Figure):
    _title = 'Квадрат'

    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 4)


class Rectangle(Figure):
    _title = 'Прямоугольник'

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return round(self.length * self.width, 4)


class Triangle(Figure):
    _title = 'Треугольник'

    def __init__(self, side_a, side_b, angle):
        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle

    def area(self):
        return round(0.5 * self.side_a * self.side_b * sin(radians(self.angle)), 4)

    @staticmethod
    def check(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False


class Trapezoid(Figure):
    _title = 'Трапеция'

    def __init__(self, upper_base, lower_base, height):
        self.upper_base = upper_base
        self.lower_base = lower_base
        self.height = height

    def area(self):
        return 0.5 * self.height * (self.upper_base + self.lower_base)


class Rhomb(Figure):
    _title = 'Ромб'

    def __init__(self, side, angle):
        self.side = side
        self.angle = angle

    def area(self):
        return round(self.side ** 2 * sin(radians(self.angle)), 4)


class Circle(Figure):
    _title = 'Круг'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 4)


class Pyramid(Figure3D):
    _title = 'Пирамида'

    def __init__(self, base_side, height):
        self.base_side = base_side
        self.height = height

    def area(self):
        return round((self.base_side * 4) / 2 * sqrt((self.height ** 2) +
                                                     (self.base_side / (2 * tan(radians(180 / 4)))) ** 2), 4)

    def volume(self):
        return round((1 / 3) * self.height * self.base_side ** 2, 4)


class Cube(Figure3D):
    _title = 'Куб'

    def __init__(self, side):
        self.side = side

    def area(self):
        return round(6 * self.side ** 2, 4)

    def volume(self):
        return round(self.side ** 3, 4)


class Sphere(Figure3D):
    _title = 'Сфера'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(4 * pi * self.radius ** 2, 4)

    def volume(self):
        return round((4/3) * pi * self.radius ** 3, 4)


class Parallelepiped(Figure3D):
    _title = 'Параллелепипед'

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return round(2 * (self.length * self.width + self.length * self.height + self.height * self.width), 4)

    def volume(self):
        return round(self.length * self.width * self.height, 4)


class Cylinder(Figure3D):
    _title = 'Цилиндр'

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def area(self):
        return round(2 * pi * self.radius * (self.radius + self.height), 4)

    def volume(self):
        return round(pi * (self.radius ** 2) * self.height, 4)


class Cone(Figure3D):
    _title = 'Конус'

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def area(self):
        return round(pi * self.radius * sqrt(self.radius ** 2 + self.height ** 2), 4)

    def volume(self):
        round((1/3) * (pi * (self.radius ** 2) * self.height), 4)

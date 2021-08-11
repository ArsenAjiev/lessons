"""
Создать класс Point, описывающий точку (атрибуты: x, y).
Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы:
нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
 Square (атрибуты: две точки, методы: нахождение площади и периметра).
 При потребности создавать все необходимые методы
 не описанные в задании
"""

# задавал параметры фигур в виде длинны отрезков.
# не получилось работать с координатами.

import math


class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


# для перебора методов фигур в цикле
# необходимо создать аналогичный метод в родительском классе
class Figure:
    def area(self):
        return f" the area of the figure"

    def perimeter(self):
        return f" the perimeter of the figure"


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    # площадь круга
    def area(self):
        s = math.pi * (self.radius ** 2)
        return f" area of circle is {s}"

    # периметр круга
    def perimeter(self):
        p = 2 * math.pi * self.radius
        return f" perimeter of circle is {p}"


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # площадь треугольника
    def area(self):
        half_per = (self.a + self.b + self.c) / 2
        s = math.sqrt(half_per * (half_per - self.a) * (half_per - self.b) * (half_per - self.c))
        return f" area of triangle is {s}"

    # периметр треугольника
    def perimeter(self):
        p = self.a + self.b + self.c
        return f" perimeter of triangle is {p}"


class Square(Figure):
    def __init__(self, a):
        self.a = a

    # площадь квадрата
    def area(self):
        s = self.a ** 2
        return f" area of square is {s}"

    # периметр квадрата
    def perimeter(self):
        p = 4 * self.a
        return f" perimeter of square is {p}"

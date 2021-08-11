"""
Создать список фигур и в цикле подсчитать и вывести
площади всех фигур на экран.
"""

from solution_1 import Triangle
from solution_1 import Circle
from solution_1 import Square


# создаем список фигур
if __name__ == "__main__":
    triangle = Triangle(a=3, b=4, c=5)
    circle = Circle(radius=4)
    square = Square(a=5)

# перебираем медоды нахождения площади фигуры.
# выводим на печать площадь фигур.
    for Figure in [triangle, circle, square]:
        print(Figure.area())


# area of triangle is 6.0
# area of circle is 50.26548245743669
# area of square is 25


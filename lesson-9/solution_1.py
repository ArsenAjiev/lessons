"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).
"""


class Car():
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    # метод увеличения скорости на 5 км.
    def increase_speed(self):
        self.speed = self.speed + 5

    # метод уменьшения скорости на 5 км.
    def reduse_speed(self):
        self.speed = self.speed - 5

    # метод остановки - скорость  = 0.
    def stop(self):
        self.speed = 0

    # метод указывает текущую скорость.
    def current_speed(self):
        print(f"current speed is {self.speed}")

    # метод движения задним ходом, замена знака на противполжный.
    def cer_reversed(self):
        self.speed = -(self.speed)

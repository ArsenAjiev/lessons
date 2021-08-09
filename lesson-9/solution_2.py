"""
Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes,
модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран
"""


# функция создает объетт класса с заданными параметрами.
def car_create():
    from solution_1 import Car
    mersedes = Car(brand="Mersedes", model="E500", year=2000)
    # увеличение скорости методом mersedes.increase_speed()
    # до тех пор, пока скорость не достигнет 100 км.
    while mersedes.speed != 100:
        mersedes.increase_speed()
    return print(f" {mersedes.brand} набрал скорость {mersedes.speed} км")


def main():
    # запуск программы
    car_create()


if __name__ == "__main__":
    main()

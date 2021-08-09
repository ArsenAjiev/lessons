"""
Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
Создать функцию, которая возвращает новый список со всеми машинами,
год выпуска которых больше Х

"""
car_list = [
    {"sn": 4435, "color": "red", "year": 1998},
    {"sn": 6935, "color": "green", "year": 2010},
    {"sn": 567, "color": "black", "year": 1988},
    {"sn": 1185, "color": "grey", "year": 1976}
]


def filter_cars(year):
    result = []
    for car in car_list:
        if car["year"] > year:
            result.append(car)
    return result


def main():
    year = 2000
    filtered_cars = filter_cars(year)
    print(filtered_cars)


if __name__ == "__main__":
    main()
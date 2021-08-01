""""
Дан список стран и городов каждой страны, где ключи это названия стран,
а значения - списки городов в этих странах. Написать функцию которая
осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну

"""

def country(spis):
    choise_city = input("Введите название города: ")
    #  циклом проверяем наличие введенной перемнной в значениях словаря.
    for key, value in spis.items():
        if choise_city in value:
           print(f" город - {choise_city}, страна -  {key} ")



dic2 = {
    "Span": ("Madrid", "Barcelona", "Valencia"),
    "France": ("Paris", "Marseille", "Lion"),
    "Italy": ("Roma", "Milano", "Napoli")
}
country(dic2)

#  Введите название города: Barcelona
#   город - Barcelona, страна -  Span


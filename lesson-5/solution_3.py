# """
# Написать функцию, которя используя модуль requests скачивает файл и сохраняет его
# на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе.
# В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из Вашего репозитория.
# """
#
# import requests
#
# def save_from_www(link):
#     """разбиваем строку на части используя раэделитель ('/') что бы получить название файла.
#     последний элемент с конца списка
#     """
#     filename = link.split('/')[-1]
#     links = link  #  ссылка на файл
#     #  получаем данные используя метод (get)
#     r = requests.get(link)
#     #  записываем полученные даннные в файл
#     open(filename, "wb").write(r.content)
#     return filename, links
#
#
# link1 = 'https://github.com/ArsenAjiev/lesson-2n/blob/master/LICESE.txt'
#
# save_from_www(link1)
# print(save_from_www(link1))


import requests


def download_file(link, name):
    r = requests.get(link)
    open(name, "wb").write(r.content)


download_file("https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE", "LICENSE")




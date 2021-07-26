"""
Написать функцию, которя используя модуль requests скачивает файл и сохраняет его
на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из Вашего репозитория.
"""
import requests

def save_from_www(link):
    filename = link.split('/')[-1]
    links = link
    #print(filename)
    r = requests.get(link)
    open(filename, "wb").write(r.content)
    return filename, links

link1 = 'https://github.com/ArsenAjiev/lesson-2n/blob/master/LICESE.txt'

save_from_www(link1)
print(save_from_www(link1))


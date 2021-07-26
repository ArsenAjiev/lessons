""" Написать функцию, которая получает на вход имя и выводит строку вида:
f " Hello {name} ". Создать список из 5 имен. Вызвать функцию для каждого
элемента списка в цикле
"""


def format_string(name):
    return f"Hello, {name}"


my_names = ["Alex", "Olga", "Roma", "qwerty"]

for me_name in my_names:
    my_string = format_string(my_names)

print(my_names)

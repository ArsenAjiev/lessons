"""
Создайте функцию three_args() которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводяться значения переданных переменных,
но только если они не равны None. Получим следующее сообщение:
Преданные арументы: var1 = 2, var3 = 10.
 """
def three_args(var1 = None, var2 = None, var3 = None):
    if var1 == None:
        print(f'var2 = {var2}, var3 = {var3}')
    elif var2 == None:
        print(f'var1 = {var1}, var3 = {var3}')
    elif var3 == None:
        print(f'var1 = {var1}, var2 = {var2}')
    else:
        print(f'var1 = {var1}, var2 = {var2}, var3 = {var3}')


three_args(var1 = 12, var3 = 110)


""" Нашел в интернете, но не понял функцию local().item() и (*) как отдельный аргумент!

def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

# Тесты
three_args(var1=21)
three_args(var1='Python', var3=3)
three_args(var1='Python', var2=3, var3=9)

"""

# правильный ответ

def three_args(*args, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            print(f"{key} = {value}")


three_args(var1=2, var3=10)


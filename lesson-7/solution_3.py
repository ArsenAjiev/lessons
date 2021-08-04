"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так,
чтобы они не били друг друга (ферзь может ходить по горизонтали,
вертикали и диагонали). Вам дана расстановка двух ферзей на доске,
определите могут ли ферзи бить друг друга. Программа получает на вход
две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если ферзи не бьют друг друга,
выведите слово NO, иначе выведите YES.
"""


n = 2  #  количество ферзей на поле
x = []
y = []
"""
Вводим пары чисел "x" и "y" через пробел поочереди для каждого ферзя.
Нажимаем "Ввод"
"""
for i in range(n):
    new_x, new_y = [int(s) for s in input("Ведите координаты ферзя: ").split()]
    x.append(new_x)
    y.append(new_y)

"""
Проверка условий: 
 1. - x[i] == x[j] - ферзи находятся на одной вертикали,
 2. - y[i] == y[j] - ферзи находятся на одной горизонтали,
 3. - abs(x[i] - x[j]) == abs(y[i] - y[j]) - ферзи находятся на одной диогонали.
"""
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')

    """ Пример выполнениея кода:
     Ведите координаты ферзя: 2 3 
     Ведите координаты ферзя: 6 7 
     YES
    """
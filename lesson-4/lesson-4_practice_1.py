""" Дан произвольный список содержащий только числа.
Выведите результат сложения всех чисел больше 10 """

import random
my_list = []
count = 0
for _ in range(10):
    my_list.append(random.randint(0, 100))
    count += 1
my_summ = 0
for element in my_list:
    if element >= 10:
        my_summ = my_summ + element


print(my_summ)
print(count)
print(my_list)


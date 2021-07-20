""" Получить сумму кубов натуральных чисел от n до m
используя цикл for, числа n и m вводятся с клавиатуры."""

my_str_1 = input()
n = int(my_str_1)

my_str_2 = input()
m = int(my_str_2)

my_summ = 0

for element in range(n, m + 1):
    my_pdw = element ** 3
    my_summ = my_summ + my_pdw

print(my_summ)

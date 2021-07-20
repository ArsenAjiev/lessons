""" Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n
(вкключая n) используя цикл while"""

my_str = input()
my_int = int(my_str)

counter = 0
my_summ = 0

while counter <= my_int:
    my_pwd = counter ** 3
    my_summ = my_summ + my_pwd
    counter += 1

print(my_summ)
print(counter)
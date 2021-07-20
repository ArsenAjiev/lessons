""" Ввести с клавиатуры строку. Проверить является ли строка палиндропом
 и вывести результат yes/no  на экран"""

my_str = str(input())
x = len(my_str)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if my_str[x - i] == my_str[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")
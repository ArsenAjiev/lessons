# 7.Извлечь элементы из списка со 2-го по 4-й, вывести их в обратном порядке.
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
#          0 - 1 - 2 - 3 - 4 -   5 -       6    -      7

# индекс 2 = 2; индекс 5 = "python" - не учитывается!!!берет индекс 4 = 5.0
new_my_list = (my_list[2:5])  # [2, 2, 5.0]

# [::-1] после строкой - создает перевернутую копию
new_my_list_revers = (my_list[2:5][::-1])
# или
new_my_list_revers_2 = new_my_list[::-1]

print(new_my_list_revers)
print(new_my_list_revers_2)

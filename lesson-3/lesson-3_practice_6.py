# 6.Найти в списке ниже количество не уникальных элементов.
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
print(len(my_list))  # длинна всего списка = 8
print(set(my_list))  # список уникальных значений = {1, 2, 5.0, 'python', 'python3'} = 5

count_non_unique_elements = len(my_list) - len(set(my_list))  # 8 - 5 = 3
print(count_non_unique_elements)  # 3

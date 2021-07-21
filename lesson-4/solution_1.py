""" Дан список my_list = [1, 1, 3, 5, 8, 13, 21, 34, 55, 89]
выведете все элементы которые меньше 5"""

my_list = [1, 1, 3, 5, 8, 13, 21, 34, 55, 89]
new_my_list = []

for x in my_list:
    if x < 5:
        new_my_list.append(x)

print(new_my_list)

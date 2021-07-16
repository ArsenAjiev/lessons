"""3.Создать список состоящий из отдельных единичныч символов,
преобразовать список в сторку инвертировать и вывести на печать. """

my_list = [1, 24, "d", "w", "l", 15]
print(my_list)  # [1, 24, 'd', 'w', 'l', 15]
print(type(my_list))  # <class 'list'>
my_list_str = str(my_list)  # преобразовали в строку.
print(type(my_list_str))  # <class 'str'>
inv_my_list_str = my_list_str[::-1]
print(inv_my_list_str)  # ]51 ,'l' ,'w' ,'d' ,42 ,1[

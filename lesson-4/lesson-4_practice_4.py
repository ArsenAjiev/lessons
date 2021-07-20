import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_element = random.choice(my_list)

while my_element != 7:
    my_element = random.choice(my_list)
    print(my_element)
    if my_element == 7:
        break





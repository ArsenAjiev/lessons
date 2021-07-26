"""

"""
import random


def search_sum_and_max(*args):
    args_summ = 0
    max_el = args[0]
    for element in args:
        if element > max_el:
            max_el = element
        args_summ += element
    return args_summ, max_el


random_element = []
for _ in range(10):
    random_element.append(random.randint(1, 100))

args_summ, max_el = search_sum_and_max(*random_element)
print(args_summ, max_el)

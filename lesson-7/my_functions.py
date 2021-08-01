def my_sum(left, right):
    return left + right


def my_pwr(value, power):
    return value ** power


def my_sum_and_pwr(left, right, power):
    value = my_sum(left, right)
    return my_pwr(value, power)
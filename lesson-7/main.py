from my_functions import my_sum_and_pwr


def main():
    var_1 = int(input("Enter first value: "))
    var_2 = int(input("Enter second value: "))
    power = int(input("Enter power: "))
    result = my_sum_and_pwr(var_1, var_2, power)
    print("Result: ", result)


if __name__ == "__main__":
    main()


# Decorator function
def my_decorator(func):
    def silencer(bullet, gunpowder):
        sound_level = func(bullet, gunpowder)
        return sound_level - 10
    return silencer


@my_decorator
def my_gun(bullet, gunpowder):
   return bullet + gunpowder


result = my_gun(3, 14)
print(result)
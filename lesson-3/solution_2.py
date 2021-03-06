""" Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10 процентов годовых
(каждый год размер вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада
и на рих в следующем году тоже будут проценты).
   1. Рассчитать сумму на счету пользователя по окончанию вклада и вывести на печать, если в
   конце каждого года ему начисляется бонус в размере 120 руб."""

deposit = 2130
interest_rate = 10
time = 5
bonus = 120

# Рассчет без бонуса
summ_deposit = deposit * (1 + interest_rate / 100)**5
print(summ_deposit)  # 3430.386300000001

# Рассчет с бонусом
summ_year_1 = deposit * (1 + interest_rate / 100)**1 + 120  # сумма с процентами за год + бонус
print(summ_year_1)    # 2463.0

summ_year_2 = summ_year_1 * (1 + interest_rate / 100)**1 + 120  # с нарастающим итогом + бонус
print(summ_year_2)    # 2829.3

summ_year_3 = summ_year_2 * (1 + interest_rate / 100)**1 + 120  # с нарастающим итогом + бонус
print(summ_year_3)    # 3232.2300000000005

summ_year_4 = summ_year_3 * (1 + interest_rate / 100)**1 + 120  # с нарастающим итогом + бонус
print(summ_year_4)    # 3675.453000000001

summ_year_5 = summ_year_4 * (1 + interest_rate / 100)**1 + 120  # с нарастающим итогом + бонус
print(summ_year_5)    # 4162.998300000001 - сумма за 5 лет.





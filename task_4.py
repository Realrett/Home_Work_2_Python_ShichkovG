# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = float(input('Введите  число: '))
summ = 0
res = 0
n = 1
while n <= number:
     res = (1+1/n)**n
     summ = summ + res
     n = n + 1
print('Сумма чисел последовательности: ')
print(summ)
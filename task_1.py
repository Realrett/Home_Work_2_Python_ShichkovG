# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = int(input('Введите вещественное число: '))
summ = 0
while number > 0:
    digit = number % 10
    summ = summ + digit
    number = number // 10
print('Сумма цифр числа раван: ')
print(summ)
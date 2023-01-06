# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('Введите число: '))
result = 1
n = 1

while n <= number:
   result = n*result
   print(result)
   n = n + 1
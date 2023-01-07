# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке
# ( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1]

import random
n = int(input('Введите число: '))
mas = [random.randint(-n, n) for i in range(n)]
print(mas)
mas2 = [random.randint(0, n-1) for i in range(2)]
print(mas2)
mult = mas[mas2[0]] * mas[mas2[1]]
print(mult)
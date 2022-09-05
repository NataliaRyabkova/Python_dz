# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
numbers = []
for i in range(5):
    numbers.append(randint (-5,5))
print(f"Заданный список: ", numbers)

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элементаt: '))

for i in range(len(numbers)):
    proizvedenie = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов на указанных позициях равно:', proizvedenie)
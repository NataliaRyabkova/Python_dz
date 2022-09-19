# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


from math import factorial

m = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
lst = list( f(i) for i in range(1, m +1))
print(lst)
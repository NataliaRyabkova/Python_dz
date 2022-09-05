# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число N: '))
factorial = 1
for i in range(1, num+1):
    factorial *= i
    print(factorial, end=' ')
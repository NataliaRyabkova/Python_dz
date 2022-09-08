# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def fibonacci(n):
    num = []
    a = 1
    b = 1
    for i in range(n):
        num.append(a)
        a, b = b, a + b
    a = 0
    b = 1
    for i in range (n+1):
        num.insert(0, a)
        a, b = b, a - b
    return num

print(fibonacci(n))




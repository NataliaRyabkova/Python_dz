# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def num(n):

    return[round((1 + 1 / x)**x, 1) for x in range (1, n + 1)]   
        
print(num(n))
print(sum(num(n)))

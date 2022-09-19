#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from functools import reduce

list1 = [1.1, 1.2, 3.1, 5, 10.01]
result = reduce(lambda x, y: x if x % 1> y % 1 else y, list1)
result1 = reduce(lambda x, y: x if x % 1 < y % 1 else y, list1)
n = result % 1 - result1 % 1
print (f"Разница между максимальным и минимальным значением дробной части равна: {n} ")

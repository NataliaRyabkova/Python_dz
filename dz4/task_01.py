#Вычислить число c заданной точностью d Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d =  int(input("Введите число d для определения точности: "))
# print(f'Число pi равно {round(pi, d)}')


import math

d = input('Введите число d указывающее степень округления числа pi ')
d = d[2:len(d)]
print(round(math.pi,len(d)))
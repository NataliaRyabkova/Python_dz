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



#def fib(n):
#   if n in [1, 2]:                       
#       return 1
#   else:
#       return fib(n-1) + fib(n-2)

#def otrfib(n):
#   if n == 1:                       
#       return 1
#   elif n == 2:                       
#       return -1
#  else:
#        a, b = 1, -1
#        for i in range(2, n):
#            a, b = b, a - b
#       return b

#list = []
#n = int(input('Введите число: '))
#for x in range(1, n + 1):
#    list.append(fib(x))
#    list.insert(0, otrfib(x))
#print(list)



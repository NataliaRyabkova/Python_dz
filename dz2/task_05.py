# Реализуйте алгоритм перемешивания списка.

import random
def Llist(list):
    list = ['Задача номер 5','Мир', 178, 'Число Пи', 2022]
    list1 = len(list)
    for i in range(list1):
        index = random.randint(0, list1 - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

list2 = Llist(list)
print(f"Перемешанный список равен: ", list2)
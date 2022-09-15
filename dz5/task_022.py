# Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Подумайте как наделить бота ""интеллектом""

from random import randint

def nachalo(name):
  x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
  return x
    
def xod_igroka(name, n, count, m):
    print(f"Ход {name}, он(а) взял(а) {n} конфет, теперь у {name} {count} конфет. На столе осталось {m} конфет.")
    
def hod_SuperBot(m):
    n = randint(1,29)
    while m-n <= 28 and m > 29:
        n = randint(1,29)
    return n
    

igrok1 = input("Игрок введите свое имя: ")
igrok2 = "SuperBot"
print(f'Очень приятно, сегодня Вы играете с искуственным  {igrok2}')
m = int(input("Введите количество конфет на столе: "))
ochered = randint(0,2) 
if ochered:
    print(f"Начинает играть {igrok1}")
else:
    print(f"Начинает играть {igrok2}")

count1 = 0 
count2 = 0
count = 0
countb = 0
sumcount = 0

while m > 28:
    if ochered:
        n = nachalo(igrok1)
        count1 += n
        m -= n
        count +=1
        ochered = False
        xod_igroka(igrok1, n, count1, m)
        print(f"SuperBot считает шаги, {igrok1} Это ваша попытка номер {count}")
    else:
        n = hod_SuperBot(m)
        count2 += n
        m -= n
        countb +=1
        ochered = True
        xod_igroka(igrok2, n, count2, m)
        print(f"У SuperBot это  попытка номер {countb}")
sumcount = count + countb


if ochered:
    print(f"Поздравляем, выиграл(а) {igrok1}")
else:
    print(f"Поздравляем, выиграл(а) {igrok2}")
print (f"Общее число ходов {sumcount}")
                    
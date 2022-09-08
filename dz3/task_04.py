# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

dvoichnoe = ""
dec = int(input("Введите десятичное число:\n"))
while dec != 0:
    dvoichnoe = str(dec%2) + dvoichnoe
    dec //= 2
print(dvoichnoe)
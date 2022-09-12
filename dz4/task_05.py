# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from pickletools import string1


file1 = open('file2.txt', 'w')
file2 = open('file3.txt', 'w')
ex1 = '3* x ^ 2 + 15 * x + 11 = 0'
ex2 = '2 * x ^ 2 + 7 * x + 5 = 0'
file1.write(ex1)
file2.write(ex2)
file1.close()
file2.close()

f1 = open('file2.txt', 'r')
f2 = open('file3.txt', 'r')
str1 = f1.readline()
str2 = f2.readline()

res = []
pol = ''


def razdelit(str):
    str = str.replace(' ', '')
    m = str.split('+')
    return m


def sozdanie(m):
    res= []
    for i in range(0, len(m)):
        l = ''
        l1 = m[i]
        for i in range(0, len(l1)):
            if l1[i].isdecimal():
                l += l1[i]
            else:
                break
        res.append(l)
    return res


def note(ar1, ar2):
    a = (len(ar1) - len(ar2))
    for i in range(0, len(ar1)):
        if a > 0:
            res.append(int(ar1[i]))
        else:
            res.append(int(ar1[i]) + int(ar2[-a]))
        a -= 1
    return res


m1 = razdelit(str1)
m2 = razdelit(str2)
m3 = sozdanie(m1)
m4 = sozdanie(m2)

if len(m3) == len(m4):
    for i in range(0, len(m3)):
        res.append(int(m3[i]) + int(m4[i]))
elif len(m3) > len(m4):
    res = note(m3, m4)
elif len(m3) < len(m4):
    res = note(m3, m4)

for i in range(len(res) - 1, -1, -1):
    if i > 1:
        pol += str(res[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        pol += str(res[-(i + 1)]) + ' * x + '
    elif i == 0:
        pol += str(res[-(i + 1)]) + ' = 0'

pol1 = open('filesum.txt', 'w')
pol1.write(pol)

print(pol)
pol1.close()
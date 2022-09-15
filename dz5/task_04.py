# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.


file5 = open('file5.txt', 'w')
ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
file5.write(ex5)
file5.close()


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            num += txt[i]
        else:
            res = res + txt[i] * int(num)
            num = ''
    return res

pol6 = open('file6.txt', 'w')
coding (ex5)
pol6.write(coding(ex5))

print(coding(ex5))
print(decoding(coding(ex5)))
pol6.close()
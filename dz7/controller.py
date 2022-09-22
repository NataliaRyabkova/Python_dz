from importd import importd
from exportd import exportd
from printd import printd
from quest import quest


def inputd():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите примечание: ")
    return [surname, name, phone, comment]



def separator():
    sep = input("Введите разделитель, в каком формате записывать данные: ")
    if sep == "":
        sep = None
    return sep

def choose():
    print("Выберите вариант работы со справочником:\n\
    1 - записать новый контакт;\n\
    2 - показать все контакты;\n\
    3 - найти контакт")
    n = input("Введите выбранный вариант: ")
    if n == '1':
        sep = separator()
        importd(inputd(),sep)
    elif n == '2':
        data = exportd()
        printd(data)
    else:
        word = input("Введите данные для поиска: ")
        data = exportd()
        item = quest(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*80)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")
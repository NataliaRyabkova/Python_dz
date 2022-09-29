import csv
import os.path
import logger as lg


db_file_name = ''
db = []
global_id = 0  


def init_data_base(file_name='base_phone.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()

def create(name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("такого имени нет")
        return
    if(surname == ''):
        print("такой фамилии нет")
        return
    if(number == ''):
        print("такого телефона нет")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number):
            print("контакт создан ранее")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result



def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)
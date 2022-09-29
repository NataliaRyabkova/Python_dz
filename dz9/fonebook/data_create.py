
database = {}
db = {'workers':1, 'workers_children':2, 'adress':3,'office_place':4}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))

def print_childrens(second_name):
    id = [i[0] for i in database[db['workers']] if second_name in i][0]
    deti = [i for i in database[db['workers_children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

def print_working_place(second_name):
    id = [i[0] for i in database[db['workers']] if second_name in i][0]
    deti = [i for i in database[db['office_place']] if id == i[0]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

def print_adress(city):
    id = [i[2] for i in database[db['workers']] if city in i][0]
    gorod = [i for i in database[db['adress']] if id == i[0]]
    print(*[' '.join(i[0:4]) + '\n' for i in gorod])

reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
reading_file_to_dict(4)
print(database)
print_childrens('Maksimov')
print_adress('Rostov-on-Don')
print_working_place('Maksimov')
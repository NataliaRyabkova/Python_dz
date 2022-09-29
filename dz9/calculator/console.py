def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число, по образцу "a + bj"):')
        left = get_value()
        print('Введите второе число, по образцу "a + bj"):')
        right = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число, по образцу "a/b"):')
        left = get_value()
        print('Введите второе число, по образцу "a/b"):')
        right = get_value()
        print('Выберите действие +,-,*,/:')
        oper = get_value()
    return (data_type, left, oper, right)
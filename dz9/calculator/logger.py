
from datetime import datetime as dt
from time import time


def result_logger(data, result):
    left, oper, right = data
    data_str = f'{str(left)} {oper} {str(right)}'
    time = dt.now().strftime('%H:%M')
    
    with open('calk.csv', 'a', encoding='UTF-8') as file:
        file.write('{}; операция : {} результат :{}\n'.format(
            time, data_str, result))
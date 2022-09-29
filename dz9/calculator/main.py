from calc import Calc_block as calc
from logger import result_logger as write_log
import datatransf as d_t
import console as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = calc(j)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()

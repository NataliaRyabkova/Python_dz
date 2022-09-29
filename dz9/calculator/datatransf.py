import console as c_ui
from fractions import Fraction
import cmath
from calc import Calc_block as calc
import datatransf as d_t


def data_formatting(data):
    data_type, left, oper, right = data

    if data_type == '1':

        left = complex(left)

        right = complex(right)

    elif data_type == '2':

        a = left
        left = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = right
        right = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (left, oper, right)
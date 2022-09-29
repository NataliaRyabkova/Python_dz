import cmath

def Calc_block(data):
    left, oper, right = data
    if oper == '+':
        return sum(left, right)
    if oper == '-':
        return sub(left, right)
    if oper == '*':
        return mult(left, right)
    if (oper =='/') and (right != 0):
        return div(left, right)
    

def sum(left, right):
    return left + right

def sub(left, right):
    return left - right

def mult(left, right):
    return left * right

def div(left, right):
    return left / right
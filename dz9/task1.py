

from tkinter import *
import random
root = Tk()
root.title('Крестики-нолики')
grun = True
f = []
ccount = 0

def newg():
    for r in range(3):
        for c in range(3):
            f[r][c]['text'] = ' '
            f[r][c]['backgraunt'] = 'light grey'
    global grun
    grun = True
    global ccount
    ccount = 0

def click(r, c):
    if grun and f[r][c]['text'] == ' ':
        f[r][c]['text'] = 'X'
        global ccount
        ccount += 1
        check('X')
        if grun and ccount < 5:
            bot()
            check('O')

def check(smb):
    for n in range(3):
        checkl(f[n][0], f[n][1], f[n][2], smb)
        checkl(f[0][n], f[1][n], f[2][n], smb)
        checkl(f[0][0], f[1][1], f[2][2], smb)
        checkl(f[2][0], f[1][1], f[0][2], smb)

def checkl(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'red'
        global grun
        grun = False           

def can(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def bot():
    for n in range(3):
        if can(f[n][0], f[n][1], f[n][2], 'O'):
            return
        if can(f[0][n], f[1][n], f[2][n], 'O'):
            return
        if can(f[0][0], f[1][1], f[2][2], 'O'):
            return
        if can(f[2][0], f[1][1], f[0][2], 'O'):
            return
    for n in range(3):
        if can(f[n][0], f[n][1], f[n][2], 'X'):
            return
        if can(f[0][n], f[1][n], f[2][n], 'X'):
            return
        if can(f[0][0], f[1][1], f[2][2], 'X'):
            return
        if can(f[2][0], f[1][1], f[0][2], 'X'):
            return
    while True:
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        if f[r][c]['text'] == ' ':
            f[r][c]['text'] = 'O'
            break   

for r in range(3):
    line = []
    for c in range(3):
        b = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='light grey',
                        command=lambda r=r, c=c: click(r,c))
        b.grid(row=r, column=c, sticky='nsew')
        line.append(b)
    f.append(line)
new_b = Button(root, text='start', command=newg)
new_b.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()     
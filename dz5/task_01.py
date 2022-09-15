# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Вот текст в абвтап котором абвабвабв нужно абвктн удалить все абвгод слова, абвнт содержащие определенное сочетание  "абв"'

def udalenie_slov(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = udalenie_slov(text)
print(text)
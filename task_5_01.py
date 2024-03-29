"""
Напишіть функцію real_len, 
яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""


def real_len(text):
    return len(text.replace("\n", "").replace("\f", "").replace("\r", "").replace("\t", "").replace("\v", ""))


text = 'Alex\nKdfe23\t\f\v.\r'
print(real_len(text))
'''import re


def start():
    with open(input('Введите имя файла')) as f_in:
        d = ''
        for line in f_in:
            r = line.strip()
            d += r + ' '
        return d
#Функция убирает пробелы до знаков препинания (a строка на вход - d а выход)
def whitespace(a):
    a= a.split()
    d = []
    print(a)
    for i in range(len(a)):

        if a[i] in '.,!-?':
            d[i-1] = d[i-1] + a[i]
        else:
            d.append(a[i])
    d = ' '.join(map(str, d))
    print(d)
    return d'''

'''
def associations(raw, uniq):
    words = []
    for word in uniq:
        raw_copy = raw.copy()
        that = []
        for i in range(raw.count(word)):
            ind = raw_copy.index(word)
            raw_copy.remove(word)
            if ind != len(raw_copy) and raw_copy[ind] not in that:
                that.append(raw_copy[ind])
        words.append(that)
    return words


def unic(a):
    u = []
    b = a.split()
    for i in b:
        if i not in u:
            u.append(i)
    print(u)
    return b,u


def sort(b):
    z = []
    w = []
    for i in b:
        if i[0].isupper():
            z.append(i)
        else:
            w.append(i)
    print(z, w)
    return z, w

d=start()
d=re.sub(r'\s+(?=(?:[,.?!:;…]))', r'', d)
words,unic_words = unic(d)
u, l = sort(unic_words)
'''


#Функция выводит результат (total)
import random
total = [1, 2, 3]

empty_list = []
for i in total:
    rand_index = random.randint(0, len(empty_list))
    empty_list.insert((rand_index), i)
print(empty_list)
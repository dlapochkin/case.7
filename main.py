'''
with open('input.txt') as f_in:
    d=''
    for line in f_in:
        r=line.strip()
        d+=r+' '
    print(d)

#Функция убирает пробелы до знаков препинания (a строка на вход - d а выход)
a = input().split(' ')
d = []
print(a)
for i in range(len(a)):

    if a[i] in '.,!?':
        d[i-1] = d[i-1] + a[i]
    else:
        d.append(a[i])
d = ' '.join(map(str, d))
print(d)

#Функция выводит уникальные слова в список (u)
u=[]
b=d.split()
for i in b:
    if i not in u:
        u.append(i)
print(u)
z=[]
w=[]
for i in u:
    if i[0].isupper():
        z.append(i)
    else:
        w.append(i)
print(z,w)'''


#Функция выводит результат (total)
import random
total = []

empty_list = []
for i in total:
    rand_index = random.randint(0, len(empty_list))
    empty_list.insert((rand_index), i)
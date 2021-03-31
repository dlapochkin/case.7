#убирает пробелы перед знаком препинания
#def dlt():
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
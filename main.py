with open('input.txt') as f_in:
    d=''
    for line in f_in:
        r=line.strip()
        d+=r
    print(d)

u=[]
b=d.split()
for i in b:
    if i not in u:
        u.append(i)
print(u)

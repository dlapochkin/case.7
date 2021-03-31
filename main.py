with open('input.txt') as f_in:
    d=''
    for line in f_in:
        r=line.strip()
        d+=r+' '
    print(d)

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
print(z,w)

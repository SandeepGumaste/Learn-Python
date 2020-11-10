txt = input('Enter file name: ')
txt = txt + '.txt'
p = 0
q=0
r = list()
s = list()
m = open(txt)
n = dict()
for lx in m :
    q = q + 1
    if lx.startswith('From') :
        for ly in lx :
            s.append(lx.split())
            if s == 'Mon' or 'Tue' or 'Wed' or 'Thu' or 'Fri' or 'Sat' or 'Sun' :
                r.append(s)
            else :
                continue
        p = p + 1
    else :
        continue
print(r)

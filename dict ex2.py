txt = input('Enter file name: ')
txt = txt + '.txt'
fh = open(txt)
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
lst = list()
c = 0 #Line count
r = 0
di = dict()
for lx in fh:
    c = c+1
    if lx.startswith('From') :
        r = r + 1
        lx = lx.rstrip()
        wds = lx.split()
        for ly in wds:
            if ly in days:
                lst.append(ly)
            else:
                continue
    else:
        continue
for day in lst:
    di[day] = di.get(day,0)+1
print(di)
print('Scanned through',c,'lines')
print('Found',r,'results')

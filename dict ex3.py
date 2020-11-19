#Finding max number of emails received using dict()
txt = input('Enter file name: ')
txt = txt + '.txt'
fh = open(txt)
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
lst = list()
c = 0 #Line count
r = 0 #result count
di = dict()
for lx in fh:
    c = c+1
    if lx.startswith('From') :
        r = r + 1
        lx = lx.rstrip()
        wds = lx.split()
        lst.append(wds[1])
for mail in lst:
    di[mail] = di.get(mail,0) + 1
print(di.items())
print(di.keys())
for k,v in di.items():
    if v is max(di.values()):
        print('Max e-mails received fron :',k)
        print('Number of e-mails received:',v)
    else:
        continue
nlst = list(di.values())
print(nlst)
nlst.sort()
print(nlst)

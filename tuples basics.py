txt = input('Enter file name: ')
txt = txt + '.txt'
fh = open(txt)
di = dict()
for lx in fh:
    lx = lx.rstrip()
    wds = lx.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
tmp = list()
for k,v in di.items():
    # print(v,k)
    nt = (v,k)
    tmp.append(nt)
tmp = sorted(tmp, reverse=True)
print(tmp[:5])


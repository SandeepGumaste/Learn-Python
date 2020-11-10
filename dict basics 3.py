fname = input('Enter file name:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
di = dict()

for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        
        di[w] = di.get(w,0) + 1
for k,v in di.items():
    if v is max(di.values()):
        print(k,v)

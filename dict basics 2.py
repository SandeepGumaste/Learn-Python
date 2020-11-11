txt = input('Enter file name: ')
txt = txt + '.txt'
fh = open(txt)
find = input('Enter the string you want to find :')
c = 0
b = 0
di = dict()
for lx in fh:
    c = c + 1
    lx = lx.rstrip()
    if len(lx) <= 1 :
        b = b + 1
        continue
    else:
        wds = lx.split()
    for ly in wds:
        di[ly] = ly
        ##Can be done using this commented way without using dictionary wich will also give the kine number
        # if ly == find:
        #     print('Found in line number',c)
        #     break
        # else:
        #     continue
if find in di:
    print('Found')
else:
    pass
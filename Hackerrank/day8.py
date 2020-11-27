#DAY 8
n = int(input())
i = 0
nl = list()
pl = list()
d = dict()
while i<n:
    np = input()
    x = np.split()
    nl.append(x[0])
    pl.append(x[len(x)-1])
    i+=1
d = {nl[k]:pl[k] for k in range(len(nl))}
i1 = 0
while i1 < n:
    name = input()
    if name not in nl:
        print('Not found')
        i1+=1
        continue
    else:
        print(name + '=' + d.get(name))
    i1+=1

#Efficient
n = int(input())
n1 = n
d = dict()
while n!=0:
    np = input()
    x = np.split()
    d.update({x[0] : x[1]})
    n-=1
while n1!=0:
    search = input()
    if search in d.keys():
        print(search + '=' + d.get(search))
    else :
        print('Not found')
    n1-=1
ssf = None
l = [20,300,45,600,451,2,52]
print(l)
for l in l :
    if ssf is None :
        ssf = l
    elif l < ssf :
        ssf = l

print('Smallest among the above numbers: ',ssf)

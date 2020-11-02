ssf = None
print('Enter 6 numbers to check the smallest among them\n')

a = input()
b = input()
c = input()
d = input()
e = input()
l =[int(a),int(b),int(c),int(d),int(e)]

for l in l :
    if ssf is None :
        ssf = l
    elif l < ssf :
        ssf = l

print('Smallest among the entered numbers: ',ssf)

#input = aaabbcccbd // output = abcbd. checking for consecutive duplicates and remove them.
x = input('Enter a string : ')
y = list(x.strip())
ya = y[1:]
m = list()
ya.append(y[0])
z = 0
l = len(y)
while z < l:
    if y[z] == ya[z]:
        pass
    else:
        m.append(y[z])
    z = z + 1
s = ''.join(m)
print('output:',s)
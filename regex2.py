import re
fh = open('mbox-short.txt')
nl = list()
c = 0
for l in fh:
    c= c + 1
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',l)
    if len(stuff) != 1 :
        continue
    else:
        num = float(stuff[0])
        print(num)
        nl.append(num)
print('Maximum:', max(nl))
##Use '\$' to find dollar sign using regex otherwise $ is used to match the end of line
x = 'we received $50 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
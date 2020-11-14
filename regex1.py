import re
x = 'my 2 fav numbers are 19 and 45'
fh = open('mbox-short.txt')
for l in fh:
    l = l.rstrip()
    if re.search('^From:', l):
        print(l)
y = re.findall('[0-9]+',x)
print(y)
z = re.findall('[AEIOU]+',x)
print(z) #No letter output brcause no uppercase vowels in x
xy = re.findall('[aeiou]+',x)
print(xy) #Lowercase vowels in x are output

#re.searchall() ----- Gives a True/False output

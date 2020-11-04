x = input('Enter a sentence or a word to get it reversed: ')
z = list(x)
a = z
y = len(z) - 1
for x in x :
    a[y] = x
    y = y - 1
print('\n The entered word/sentence in reverse is:',''.join(a))

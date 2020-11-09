counts = dict()
names = list()
x = None
print('---Enter a name to continue adding names---\n---Enter done when you are done adding names---')
while True :
    x = input('name: ')
    if x == 'done' :
        break
    else :
        names.append(x)
        continue
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts,'\n')
print(len(counts), '\n')
for key in counts :
    print(key, counts[key])

print('\n')
print('\n\n',counts.keys(), counts.values())

print('\n\n')
for aaa,bbb in counts.items() :
    print(aaa,bbb)
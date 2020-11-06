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
print(counts)
print(list(counts)) ## Found that converting the dict to list removes duplicates and gives uniques.
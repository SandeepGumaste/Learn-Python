counts = dict()
print('Enter text')
line = input('')
lst = list()
words = line.split()
print('Counting')
for word in words :
    counts[word] = counts.get(word,0) + 1
for key in counts :
    lst.append(counts[key])

for count in counts :
    if max(lst) == counts[count] :
        print(count, counts[count])
    else:
        continue
bc = None
bw = None
for word,count in counts.items() :
    if bc is None or count > bc :
        bw = word
        bc = count
print(bw, bc)

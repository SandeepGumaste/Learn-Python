file = input("Enter the text file name to read: ")
file = file + '.txt'
srch = input('Enter the search word: ')
fh = open(file) 
c = 0
cn = 0
for lx in fh :
    lx = lx.lstrip()
    if lx.startswith(srch) :
        print(lx.rstrip())
        c = c + 1
    else :
        cn = cn + 1
        continue
        
print('total results found: ', c)
print('Total number of lines read: ', c + cn)

a = input('Enter a word\n')
e = a
b = len(a) - 1
d=-1

for e in e :

    d= d + 1
    print(d,"-",e)

print('Enter a value less than or equal to',b)
print('to exract the letter\n')

while True :
    c = input()
    c = int (c)
        
    if c <= b :
        d = a [c]
        print(d)
        break

    elif c > b :
        print("Enter a value less than",b)
        continue

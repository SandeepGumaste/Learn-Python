n = input('Enter the number of words you want to enter: ')
n = int(n)
l = list()
r = None
p = l
q = list()
m = 0
while m < n :
    l.append(input('Enter word: '))
    m = m + 1
print("Initial list: ",l)

def chop() :
    p = l[1:n-1]
    print("After chop:",p)

def middle() :
    q.append(l[0])
    q.append(l[n-1])
    print(q)

while True :

    print('\n\nEnter 1 for chop()\nEnter 2 for middle()\nEnter 3 to stop')
    
    while True :
        r = input('Enter 1, 2 or 3 : ')
        try :
            r = int(r)
            break
        except :
            print('please enter number 1, 2 or 3')
            continue
    if r == 1 :
        chop()
    elif r == 2 :
        middle()
    elif r == 3 :
        print('Program stopped')
        break
    else :
        print('Invalid Entry. Please enter number 1, 2 or 3')
        continue
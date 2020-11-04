number = input('Enter number of people:')
number = int(number)
m = list()
n = None
x = 0
xx = 1
while x < number :
    xx = str(xx)
    if x == 0 :
         n = 'st' 
    elif x == 1 :
        n = 'nd'
    elif x == 2 :
        n = 'rd'
    else :
        n = 'th'

    x = x + 1    
    print('Enter', xx+n ,' name')
    m.append(input())
    xx = int(xx)
    xx = xx + 1
aa = 0
while aa < len(m):
    print('Hello, welcome to the python dungeon',m[aa])
    aa = aa + 1
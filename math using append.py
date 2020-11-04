while True :
    x = input('Enter the number of numbers you want to add: ')
    try :
        x = int(x)
        break
    except :
        print('Please enter an integer')
        continue
xx = 0
m = list()
while xx < x :
    m.append(int(input('Enter number: ')))
    xx = xx + 1

print('Maximum: ', max(m))
print('Minimum: ', min(m))
print('Total: ', sum(m))
print('Average: ', sum(m)/len(m))
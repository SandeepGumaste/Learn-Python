import random

while True:
    die = [1,2,3,4,5,6]
    m = input('Press enter to roll the dice or anything else to exit')
    if m == '':
        random.shuffle(die)
        num = random.choice(die)
        n = die.pop()
        print('die1:',num,'\ndie2:',n)
        if n + num == 6 or n + num == 12 and n == num :
            print('Play once again')
            continue
    else:
        print('Stopped')
        break
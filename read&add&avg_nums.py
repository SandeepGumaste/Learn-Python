num = 0

tot = 0.0

while True :
    sval = input ('Enter a NUMBER : ')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval

print("Total: ",tot,"\nCount: ",num,"\nAverage: ",tot/num)
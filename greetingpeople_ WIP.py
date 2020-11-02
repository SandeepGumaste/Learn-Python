while True :
    m = input('Enter number of people (max 5): ')
    try :
        m = int(m)
        if m > 5 :
            print('Enter a number less than 5')
            break
        elif m == 0 :
            print('Invalid input\nPlease enter a valid number')
            break
    except :
        print('\nInvalid Entry. Please enter a number.')

    if m == 1 :
        a = input('Enter your name: ')
        b = '-x-x-x-x-x-x-x-'
        c = '-x-x-x-x-x-x-x-'
        d = '-x-x-x-x-x-x-x-'
        e = '-x-x-x-x-x-x-x-'
        print("\nWelcome ", a)
    elif m == 2 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = '-x-x-x-x-x-x-x-'
        d = '-x-x-x-x-x-x-x-'
        e = '-x-x-x-x-x-x-x-'
        print("\nWelcome ", a)
        print("\nWelcome ", b)
    elif m == 3 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = input('Enter your name: ')
        d = '-x-x-x-x-x-x-x-'
        e = '-x-x-x-x-x-x-x-'
        print("\nWelcome ", a)
        print("\nWelcome ", b)
        print("\nWelcome ", c)
    elif m == 4 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = input('Enter your name: ')
        d = input('Enter your name: ')
        e = '-x-x-x-x-x-x-x-'

        print("\nWelcome ", a)
        print("\nWelcome ", b)
        print("\nWelcome ", c)
        print("\nWelcome ", d)
    elif m == 5 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = input('Enter your name: ')
        d = input('Enter your name: ')
        e = input('Enter your name: ')

        print("\nWelcome ", a)
        print("\nWelcome ", b)
        print("\nWelcome ", c)
        print("\nWelcome ", d)
        print("\nWelcome ", e)

    aa = input('Would you like to add more people?[y/n]\n')

    if  aa == 'y' :
        ab = a
        ac = b
        ad = c
        ae = d
        af = e
        
        continue

    elif aa == 'n' :
        print(' 1', a,'\n 2', b,'\n 3', c,'\n 4', d,'\n 5', e,'\n 6', ab,'\n 7', ac,'\n 8', ad,'\n 9', ae,'\n 10', af)
        print("\nAll Done")
        break
    else :
        print("All done")
        break

    

    
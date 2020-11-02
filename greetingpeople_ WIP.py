while True :
    a = '-x-x-x-x-x-x-x-'
    b = '-x-x-x-x-x-x-x-'
    c = '-x-x-x-x-x-x-x-'
    d = '-x-x-x-x-x-x-x-'
    e = '-x-x-x-x-x-x-x-'
    ab = '-x-x-x-x-x-x-x-'
    ac = '-x-x-x-x-x-x-x-'
    ad = '-x-x-x-x-x-x-x-'
    ae = '-x-x-x-x-x-x-x-'
    af = '-x-x-x-x-x-x-x-'
    
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
        print("\nWelcome ", a)
    elif m == 2 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        
        print("\nWelcome ", a)
        print("\nWelcome ", b)
    elif m == 3 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = input('Enter your name: ')
        
        print("\nWelcome ", a)
        print("\nWelcome ", b)
        print("\nWelcome ", c)
    elif m == 4 :
        a = input('Enter your name: ')
        b = input('Enter your name: ')
        c = input('Enter your name: ')
        d = input('Enter your name: ')
        

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
    xy = [a,b,c,d,e,ab,ac,ad,ae,af]
    aa = input('Would you like to add more people?[y/n]\n')
    
    if  aa == 'y' :
        ab = a
        ac = b
        ad = c
        ae = d
        af = e
        continue
    else :
        
        print(xy)
        # while xy in xy :
        #     if xy == '-x-x-x-x-x-x-x-' :
        #         print(xy)
        #     else :
        #         continue
                    
        #     print("\nAll Done")
    break    

    

    
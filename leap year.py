ly = 2000
a = int(input('Enter the year you want to check: '))

if a <= ly:
    f = (ly - a)/4
elif a > ly:
   f = (ly - a)/4

if f - int(f) == 0:
    print(a,'is a leap year')
else:
    print(a,'is not a leap year')
    
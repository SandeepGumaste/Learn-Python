x = 5
if x == 5:
    print("equal to 5")
if x >= 5:
    print("greater than or equal than 5")

m = input('m=\n')
m = int(m)
print(m)

if m < 10:
    print("less than 10")
    if m < 5:
        print("less than 5")
    elif m > 5:
        print("greater than 5")
elif m > 10:
    print("Greater than 10")
    if m > 15:
        print("greater than 15")
    elif m < 15:
        print("Less than 15")
print("all done")

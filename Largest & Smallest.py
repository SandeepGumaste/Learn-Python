lsf = 0 #largest so far
ssf = 0 #smallest so far
numm = 0
num = [50, 81, 112, 254, 40, 250]
numm = num
print([num])
for num in num:
    if num > lsf :
        lsf = num

print("Largest among the above numbers :", lsf)

ssf=lsf

for numm in numm:
    if numm < ssf:
        ssf = numm

print("Smallest among the above numbers :", ssf)
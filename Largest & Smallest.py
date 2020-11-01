lsf = 0 #largest so far
ssf = 0 #smallest so far
print("\n 20, 81, 112, 254, 4, 250\n")
for num in [50, 81, 112, 254, 40, 250]:
    if num > lsf :
        lsf = num

print("Largest so far :", lsf)

for num in [50, 81, 112, 254, 95, 250]:
    if num < lsf:
        lsf = num
    print(lsf, num)

print("Smallest so far:", lsf)
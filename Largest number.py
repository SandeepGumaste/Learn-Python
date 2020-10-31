lsf= 0
print("Before", lsf)
for num in [50, 81, 112, 32, 95, 250]:
    if num > lsf :
        lsf = num
    print(lsf, num)

print("After:", lsf)
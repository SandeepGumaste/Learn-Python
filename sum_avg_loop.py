total = 0
count = 0
l = [10, 30, 25, 40, 100, 154]
print("count, total, l")
for l in l :
    total = total + l 
    count = count + 1
    print(" ",count,"    ",total," ",l)
print("Sum = ", total)

print("Number count = ", count)

print("Average = ", total,"/",count)

average = float (total/count)
print("Average =", average)

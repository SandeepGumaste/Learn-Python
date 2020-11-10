x = input('Enter a string : ')
y = list(x.strip())
b = y
a = list()
z = 1
for xx in y :
    if xx == b[z] :
        z = z + 1
        continue
    else :
        a.append(xx)
        z = z + 1
        continue
print(a)
    
#     if y[z] != y[z + 1] :
#         z = z + 1
#         continue
#     else :
#         z = z + 1
#         continue
    
# print(a)
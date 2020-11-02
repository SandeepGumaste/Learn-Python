a = '   I can learn coding very easily   ' # Has 3 whitespaces in the beginning and the end
print("Str entered:",a)
b = a.lower()
print("Lowercase:",b)
c = a.upper()
print("Uppercase:",c)

d = a.replace('a','xx')
print('New str :',d)

d = a.lstrip()
print("before lstrip:", a)
print("after lstrip:", d)
print(a, ":before rstrip")
e = a.rstrip()
print(e,": after rstrip") 
f = a.strip()
print("before strip:--",a,"--")
print("after strip:--",f,"--")

a = input("Enter your email id : ")
atpos = a.find('@')
un = a[0:atpos]
ed = a[atpos+1 : ]

print('Username:',un)
print('email domain:',ed)
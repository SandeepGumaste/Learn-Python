m = 'Enter an integer or a Word\n'
m = input(m)

try :
    m = int(m)
    print("Integer")

except :
    print("String detected")

print("\n Over and out")
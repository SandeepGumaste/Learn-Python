if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l1 = list()
    s =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    for m in s:
        if sum(m)!=n:
            l1.append(m)
    print(l1)

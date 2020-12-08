if __name__ == '__main__':
    N = int(input())
    lst = list()
    for i in range(N):
        cmd = list(input().split())
        if cmd[0] == 'insert':
            x = int(cmd[1])
            y = int(cmd[2])
            lst.insert(x, y)
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()
        else :
            pass
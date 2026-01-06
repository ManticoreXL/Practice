import sys
input = sys.stdin.readline

n = int(input())

s = [0] * 21

for _ in range(n):
    op = input().split()

    if len(op) == 1:
        cmd = op[0]

        if cmd == 'all':
            for i in range(1, 21):
                s[i] = 1
        
        elif cmd == 'empty':
            for i in range(1, 21):
                s[i] = 0

    else:
        cmd, x = op[0], int(op[1])

        if cmd == 'add':
            if s[x] == 0:
                s[x] = 1
        
        elif cmd == 'remove':
            if s[x] == 1:
                s[x] = 0

        elif cmd == 'check':
            if s[x] == 1:
                print(1)
            else:
                print(0)

        elif cmd == 'toggle':
            if s[x] == 1:
                s[x] = 0
            else:
                s[x] = 1

import sys

t = int(input())

s = []

for _ in range(t):
    a = sys.stdin.readline().split()
    m = a[0]

    if m == "push":
        s.append(int(a[1]))
    elif m == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif m == "size":
        print(len(s))
    elif m == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif m == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
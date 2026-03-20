import sys

t = int(input())

s = []

for _ in range(t):
    a = sys.stdin.readline().split()
    m = a[0]

    if m == "push_front":
        s.insert(0, int(a[1]))
    elif m == "push_back":
        s.append(int(a[1]))

    elif m == "pop_front":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop(0))
    elif m == "pop_back":
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

    elif m == "front":
        if len(s) == 0:
            print(-1)
        else:
            print(s[0])
    elif m == "back":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
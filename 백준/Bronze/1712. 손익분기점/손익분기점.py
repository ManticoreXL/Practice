a, b, c = map(int, input().split())

bp = c - b

if bp <= 0:
    print(-1)
else:
    print(a//bp+1)
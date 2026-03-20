t = int(input())

for _ in range(t):
    p, m = map(int, input().split())
    d = list(range(1, m + 1))
    pm = 0
    for _ in range(p):
        a = int(input())
        if a in d:
            d.remove(a)
            pm = pm + 1
    print(p - pm)
    d.clear()
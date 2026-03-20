t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for x in range(0, m+1):
        if x*2 + (m-x)*1 == n:
            t = x
            u = m - x
    print(u, t)
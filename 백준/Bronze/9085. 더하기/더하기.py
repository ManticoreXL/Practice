n = int(input())

for _ in range(n):
    nsum = 0
    a = int(input())
    s = list(map(int, input().split()))
    for x in s:
        nsum = nsum + x
    print(nsum)
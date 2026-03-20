t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    m = s[-1] - s[0]

    print(m * 2)
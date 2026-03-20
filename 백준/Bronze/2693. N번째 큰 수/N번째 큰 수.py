t = int(input())

for _ in range(t):
    s = list(map(int, input().split()))
    s.sort()
    s = s[:8]
    print(s[-1])
n = int(input())

for x in range(n):
    v, e = map(int, input().split())
    f = 2 + e - v
    print(f)
import sys
input = sys.stdin.readline

n = int(input())

crd = []

for _ in range(n): 
    x, y = map(int, input().split())
    crd.append((x, y))

crd.sort(key=lambda x:(x[1], x[0]))

for c in crd:
    print(c[0], c[1])

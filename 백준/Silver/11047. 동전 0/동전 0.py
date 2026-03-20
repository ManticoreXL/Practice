n, k = map(int, input().split())

s = []

m = 0

for x in range(n):
    a = int(input())
    s.append(a)

s.reverse()

for x in s:
    if x <= k:
        m = m + k//x
        k = k%x

print(m)
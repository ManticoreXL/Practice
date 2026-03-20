a, b = map(int, input().split())
s = []

for x in range(1, b+1):
    for y in range(1, x+1):
        s.append(x)
        if y == x:
            break

a = a-1
b = b
rs = s[a:b]
nsum = 0

for x in range(len(rs)):
    nsum = nsum + int(rs[x])

print(nsum)
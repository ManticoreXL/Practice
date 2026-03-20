s = []

for _ in range(8):
    a = int(input())
    s.append(a)

cs = sorted(s)
cs = cs[3:]

pfs = []

for x in range(8):
    for y in range(5):
        if s[x] == cs[y]:
            pfs.append(x+1)

rs = cs[0] + cs[1] + cs[2] + cs[3] + cs[4]

print(rs)
for x in range(5):
    print(pfs[x], end = " ")
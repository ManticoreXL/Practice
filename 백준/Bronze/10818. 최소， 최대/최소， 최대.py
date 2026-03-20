a = int(input())

b = list(map(int, input().split()))

maxnum = b[0]
minnum = b[0]

for x in range(1, a):
    if b[x] > maxnum:
        maxnum = b[x]
    if b[x] < minnum:
        minnum = b[x]
        
print(minnum, maxnum)
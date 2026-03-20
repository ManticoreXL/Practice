n = int(input())
m = int(input())
nsum = 0
smin = 0

for x in range(n, m+1):
    temp = x**0.5
    if temp == int(temp):
        nsum = nsum + x
        if smin==0:
            smin = x
            
if nsum==0:
    print(-1)
else:
    print(nsum)
    print(smin)
def primecheck(n):
    if n==1:
        return False
    for x in range(2, n):
        if n%x==0:
            return False
    return True

n = int(input())
m = int(input())

psum = 0
pmin = 0

for x in range(n, m+1):
    if primecheck(x)==True:
        psum = psum + x
        if pmin==0:
            pmin = x

if psum==0:
    print(-1)
else:
    print(psum)
    print(pmin)
   
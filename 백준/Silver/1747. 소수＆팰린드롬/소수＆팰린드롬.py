import math

def primecheck(n):
    if n == 1:
        return False
    for x in range(2, int(math.sqrt(n)+1)):
        if n%x == 0:
            return False
    return True

n = int(input())

while(True):
    t = str(n)
    t = t[::-1]
    t = int(t)
    if t == n and primecheck(n)== True:
        print(n)
        exit()
    n = n + 1
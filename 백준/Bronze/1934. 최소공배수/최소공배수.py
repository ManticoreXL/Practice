import sys

def gcd(x, y):
    while y>0:
        x, y = y, x%y
    return x

def lcm(x, y):
    result = (x*y)//gcd(x, y)
    return result

t = int(input())

for x in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
        
        